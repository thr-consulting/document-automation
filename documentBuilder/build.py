from dateHelpers.date import extractDate
from models.MLFile import MLFile
from models.MLDocument import MLDocument
from models.PageResult import PageResult


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
        if (
            sortedResults[i].predictedPageNumOf
            != sortedResults[i - 1].predictedPageNumOf
        ):
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


def createDocuments(results: list[PageResult], images, fileId: str) -> MLFile:
    file: MLFile = MLFile(fileId)
    file.documents = []

    print("checking if all pages have same vendor")
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
