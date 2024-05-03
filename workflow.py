import json
from helper import createDocuments, assignPageNumbers, classify, pdf2Jpg, pdf2JpgFromURL
import tensorflow as tf
from tensorflow import keras
from Document import MyCustomDocumentEncoder, MyCustomFileEncoder
import sys
import os

print("keras version: {}".format(keras.__version__))
print("tensorflow version: {}".format(tf.__version__))
print("python version: {}".format(sys.version))


# classes
classes = ['BMO Bank', 'BMO Credit', 'CIBC Bank', 'CIBC Credit', 'RBC Bank', 'RBC Credit', 'Scotia Bank', 'Scotia Credit', 'TD Bank', 'TD Credit']

# load model 
print("\n\nloading model...")
model = tf.keras.models.load_model(os.getenv('MODEL_URL'))    

# Load your SavedModel
# saved_model_path = '/home/roland/models_2024/bigBanks_2024-05-02_9am.keras'  # Update with your actual path
# model = tf.keras.layers.TFSMLayer(saved_model_path, call_endpoint='serving_default') 
# model = tf.keras.models.load_model('/home/roland/Downloads/bigBanks_2024-05-02_9am.keras')  
model.summary()
print('model loaded\n\n')


def workflow(pdf_path= "./rb4.pdf", file_id: str = "file_id"):
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
        
    # return as json
    print("returning json object: {}".format(json.dumps(mlFile, cls=MyCustomFileEncoder)))
    return json.dumps(mlFile, cls=MyCustomFileEncoder)
