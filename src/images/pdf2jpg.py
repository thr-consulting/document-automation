import urllib
import numpy as np
from pdf2image import convert_from_path, convert_from_bytes


# url pdf to jpeg
def pdf2JpgFromURL(url: str):
    print("download pdf from url...")
    
    with urllib.request.urlopen(url) as response:
        # Read the PDF content
        pdf_content = response.read()

        # convert to jpeg
        images = convert_from_bytes(pdf_content)

        print("pdf2JpgFromURL images len: {}".format(len(images)))
        return [np.array(image) for image in images]


# file pdf to jpeg
def pdf2Jpg(pdf_path):
    images = convert_from_path(pdf_path)

    return [np.array(image) for image in images]
