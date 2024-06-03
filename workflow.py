from documentBuilder.build import createDocuments
from images.pdf2jpg import pdf2JpgFromURL
from models.MLFile import convert_to_json
from predict import classify
import tensorflow as tf
from tensorflow import keras
import sys
import os

from pageNumberHelpers.extractPageNumber import assignPageNumbers
from dotenv import load_dotenv

load_dotenv()

print("\n\n-----")
print("keras version: {}".format(keras.__version__))
print("tensorflow version: {}".format(tf.__version__))
print("python version: {}".format(sys.version))
print("-----\n")

# classes
classes = [
    "*_MB_Credit_Union_Lines",
    "ATT",
    "Access Bank",
    "Assiniboine Bank",
    "BMO Bank",
    "BMO Credit",
    "BVT",
    "Beaver",
    "Bell",
    "Big Freight",
    "Bison",
    "CAT Scale",
    "CIBC Bank",
    "CIBC Credit",
    "Caisse Bank",
    "Cambrian Bank",
    "Canadian Tire Credit",
    "Cheque",
    "Custom Transport",
    "DeckX",
    "Emax",
    "Empty Page",
    "Enbridge",
    "Enmax",
    "Epcor",
    "Fido",
    "FlyingJ",
    "Geotab",
    "High Speed Crow",
    "Koodo",
    "MB Hydro",
    "MBNA Credit",
    "Niverville Bank",
    "Noventis Bank",
    "PBX",
    "Penner International",
    "Plainsview Bank",
    "PrePass",
    "RBC Bank",
    "RBC Credit",
    "RCU Bank",
    "Rogers",
    "SCU Bank",
    "Scotia Bank",
    "Scotia Credit",
    "Searcy",
    "Shaw",
    "Steves Livestock",
    "Stride Bank",
    "Sunova Bank",
    "Sunrise Bank",
    "TD Bank",
    "TD Credit",
    "Telus",
    "TransX",
    "Valley Fiber",
    "Verizon",
    "Vivint",
    "Westoba Bank",
    "Wpg Water Waste Department",
    "tBaytel",
    "xplornet",
]

# load model
print("\n\nloading model...")
model = tf.keras.models.load_model(os.getenv("MODEL_URL"))
model.summary()


def workflow(pdf_path, file_id: str = "file_id"):
    # image2pdf
    print("converting pdf to image...")
    images = pdf2JpgFromURL(pdf_path)

    if len(images) > 5:
        print("there more than 5 images... skip processing")
        return None

    # assign classes
    print("assigning classes to each page...")
    results = None
    results = classify(model, images, classes)

    # assign page numbers
    print("\nassigning page numbers...")
    assignPageNumbers(results, images)
    print("\nafter assignPageNumbers...")
    for result in results:
        print("{} {} {}".format(result.className, result.predictScore, result.predictedPageNum))
    print("-------------\n")

    # create document(s)
    print("creating documents...")
    mlFile = createDocuments(results, images, file_id)
    print("\n---\nfile id: {}".format(mlFile.id))
    print("all sorted: {}".format(mlFile.allSorted))
    for i in mlFile.documents:
        print(i.className, i.date, i.pages)

    if mlFile.allSorted:
        json = convert_to_json(mlFile)
        print("json: {}".format(json))
        return json

    return None
