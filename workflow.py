from documentBuilder.build import createDocuments
from images.pdf2jpg import pdf2JpgFromURL
from models.MLFile import convert_to_json
from predict import classify
import tensorflow as tf
from tensorflow import keras
import sys
import os
import json
from pageNumberHelpers.extractPageNumber import assignPageNumbers
from dotenv import load_dotenv

# to make sure it only uses a cpu
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

load_dotenv(".env")
MODEL_PATH = os.environ["MODEL_PATH"]
print("model path: {}".format(MODEL_PATH))

print("\n\n-----")
print("keras version: {}".format(keras.__version__))
print("tensorflow version: {}".format(tf.__version__))
print("python version: {}".format(sys.version))
print("-----\n")

# classes
classes = json.load(open('classes.json'))
print(classes)

# load model
print("\n\nloading model...")
model = tf.keras.models.load_model(MODEL_PATH)
model.summary()
print("input shape: {}: ".format(model.input_shape))

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
