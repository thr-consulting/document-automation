from data.layouts import Coordinate
import pytesseract
print("pytesseract version: {}".format(pytesseract.get_tesseract_version()))

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
    print("OCR text: {}".format(text))

    # Return the extracted text
    return text