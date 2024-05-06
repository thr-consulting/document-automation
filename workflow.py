import json
from documentBuilder.build import createDocuments
from images.pdf2jpg import pdf2JpgFromURL
from models.MLFile import MyCustomFileEncoder
from predict import  classify
import tensorflow as tf
from tensorflow import keras
import sys
import os

from pageNumberHelpers.extractPageNumber import assignPageNumbers
print('\n\n-----')
print("keras version: {}".format(keras.__version__))
print("tensorflow version: {}".format(tf.__version__))
print("python version: {}".format(sys.version))
print('-----\n')

# classes
classes = ['BMO Bank', 'BMO Credit', 'CIBC Bank', 'CIBC Credit', 'RBC Bank', 'RBC Credit', 'Scotia Bank', 'Scotia Credit', 'TD Bank', 'TD Credit']

# load model 
print("\n\nloading model...")
model = tf.keras.models.load_model(os.getenv('MODEL_URL'))    
model.summary()


def workflow(pdf_path, file_id: str = "file_id"):
    # image2pdf
    print('converting pdf to image...')
    images = pdf2JpgFromURL(pdf_path)

    # assign classes
    print('assigning classes to each page...')
    results = None
    results = classify(model, images, classes)
        
    # assign page numbers
    print("assigning page numbers...")
    assignPageNumbers(results, images)

    # create document(s)
    print("creating documents...")
    mlFile = createDocuments(results, images, file_id)
    print("\n---\nfile id: {}".format(mlFile.id))
    print("all sorted: {}".format(mlFile.allSorted))
    for i in mlFile.documents:
        print(i.className, i.date, i.pages)
        
    
    if mlFile.allSorted:
        # return as json
        print("returning json object: {}".format(json.dumps(mlFile, cls=MyCustomFileEncoder)))
        return json.dumps(mlFile, cls=MyCustomFileEncoder)
    
    return None
