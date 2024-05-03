import numpy as np
import re
from layouts import Coordinate, DateRegex, Layout, PageRegex, getLayout
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes
from Document import MLDocument, MLFile
from PageResult import PageResult
from datetime import date
import tensorflow as tf
import urllib


print("\npytesseract version: {}\n".format(pytesseract.get_tesseract_version()))


# url pdf to jpeg
def pdf2JpgFromURL(url: str):
    # download pdf
    with urllib.request.urlopen(url) as response:
        # Read the PDF content
        pdf_content = response.read()
        
        # convert to jpeg
        images = convert_from_bytes(pdf_content)
        
        # return as numpy array
        return [np.array(image) for image in images]

# file pdf to jpeg
def pdf2Jpg(pdf_path):
    images = convert_from_path(pdf_path)
    
    return [np.array(image) for image in images]





def extractText(image, extract: Coordinate):
    # Crop the image
    h, w, c = image.shape
    x = int(extract.x * w)
    y = int(extract.y * h)
    w = int(x + extract.w * w)
    h = int(y + extract.h * h)
    cropped_image = image[y:h, x:w]

    # Perform OCR on the cropped image
    text = pytesseract.image_to_string(cropped_image)
    print("extracted text: {}".format(text))

    # Return the extracted text
    return text






def allIncrement(results: list[PageResult]):
    if len(results) == 1:
        return True

    for i in range(1, len(results)):
        if int(results[i].predictedPageNum) != (
            1 + int(results[i - 1].predictedPageNum)
        ):
            return False

    return True


# all known pages complete the document: as in 3 of 3, so there would be at least 3 pages
def noPageMissing(results: list[PageResult]):
    if len(results) == 1:
        if results[0].predictedPageNum == 1:
            return True
        else:
            return False

    sortedResults = sorted(results, key=lambda p: p.predictedPageNum)

    allSameOf = True
    # make sure all have the same pageOf
    for i in range(1, len(sortedResults)):
        if sortedResults[i].predictedPageNumOf != sortedResults[i - 1].predictedPageNumOf:
            allSameOf = False
            break

    # make sure no pages are missing for pageOf
    if allSameOf:
        for i in range(1, len(results)):
            if int(results[i].predictedPageNum) == (
                1 + int(results[i - 1].predictedPageNum)
            ) or (
                i >= results[0].predictedPageNumOf and results[i].predictedPageNum == -1
            ):
                allSameOf = True
            else:
                return False

    return True


def allSameVendor(results: list[PageResult]):
    if len(results) == 1:
        return True

    for i in range(1, len(results)):
        if results[i].className != results[i - 1].className:
            return False

    return True


def getRegexDate(txt: str, regex: DateRegex) -> date:
    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]
    general = re.findall(regex.general_regex, txt, flags=re.IGNORECASE)
    print(general)
    if len(general) >= regex.generalPosition:
        general = general[regex.generalPosition - 1]
        print("general match: {}".format(general))

        extracted_day = int(general[regex.dayPosition - 1])
        extracted_month = months.index(general[regex.monthPosition - 1].lower()) + 1
        extracted_year = int(general[regex.yearPosition - 1])
        if extracted_year < 2000:
            extracted_year = extracted_year + 2000
        print(
            "date: {}".format(
                date(extracted_year, extracted_month, extracted_day).isoformat()
            )
        )

        return date(extracted_year, extracted_month, extracted_day)
    return None


def extractDate(className: str, images) -> date:
    # get layout
    layout: Layout = getLayout(className)

    # get which page to extract date from
    page = layout.date[0].pageNumber

    # get date text
    txt = extractText(images[page - 1], layout.date[0])

    # get actual date with regex
    date = getRegexDate(txt, layout.date[0].regex)

    return date


def createDocuments(results: list[PageResult], images, fileId: str) -> MLFile:
    print("Creating documents...")
    file: MLFile = MLFile(fileId)
    file.documents = []

    if allSameVendor(results):
        # if all pages have same vendor and all pages increment by 1, then all pages are the same document
        # pdf file == 1 document
        if allIncrement(results):
            print("pdf pages all have same vendor and page #'s are incrementing")

            # extract date
            date = extractDate(results[0].className, images)
            if date:
                file.documents.append(
                    MLDocument(
                        results[0].className,
                        list(range(1, len(results) + 1)),
                        date,
                    )
                )
            file.allSorted = True

        # pdf file == 1 vendor with no pages missing
        elif noPageMissing(results):
            print("pdf pages all have same vendor, with no pages missing")

            # extract date
            date = extractDate(results[0].className, images)

            # get all valid pages
            pageNumbers = []
            for i in results:
                if i.predictedPageNum != -1:
                    pageNumbers.append(i.originalOrder)

            if date and len(pageNumbers) == results[0].predictedPageNumOf:
                file.documents.append(
                    MLDocument(results[0].className, pageNumbers, date)
                )

    return file


def classify(model, images, classes: list[str]):
    print("images: {}".format(len(images)))

    image_array = tf.image.resize(images, (384, 384))
    print("image shape: {}".format(image_array.shape))

    scores = model.predict(image_array)
    max_index = np.argmax(scores, axis=1)

    results = []
    for i in range(len(max_index)):
        class_name = classes[max_index[i]]
        score = scores[i][max_index[i]]
        results.append(PageResult(i + 1, class_name, score))
        print("class: {}\nscore: {}".format(class_name, score))

    assert len(results)

    return results
