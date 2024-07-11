import os
import json
import torch

from documentBuilder.build import createDocuments
from images.pdf2jpg import pdf2JpgFromURL
from models.MLFile import convert_to_json
from extract.pageNumber import assignPageNumbers
from pytorch import load_model, predict_images
from dotenv import load_dotenv

load_dotenv() 

os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # run on cpu

MODEL_PATH = os.environ["MODEL_PATH"]
MODEL_IMAGE_SIZE = int(os.environ["MODEL_IMAGE_SIZE"])
MODEL_CLASSES_PATH = os.environ["MODEL_CLASSES_PATH"]

print(f"pytorch version: {torch.__version__}\n")

# classes
print(f"classes path: {MODEL_CLASSES_PATH}")

try:
    classes = json.load(open(MODEL_CLASSES_PATH))
    print(f"{len(classes)} classes\n")
except Exception as e:
    print("--")
    print("Error loading the classes file")
    print(f"classes path: {MODEL_CLASSES_PATH}")
    print(e)
    print("--")

# load model
device = torch.device("cpu")

try:
    model, transform = load_model(MODEL_PATH, classes, MODEL_IMAGE_SIZE, device)
except Exception as e:
    print("--")
    print("Error in loading the model")
    print(f"model path: {MODEL_PATH}")
    print(e)
    print("--")

def workflow(pdf_path, file_id: str = "file_id"):
    images = pdf2JpgFromURL(pdf_path)

    if len(images) > 10:
        print("more than 10 images... skip processing")
        return None

    # assign classes
    results = None
    results = predict_images(model, transform, images, device, classes)

    # assign page numbers
    assignPageNumbers(results, images)

    # create document(s)
    mlFile = createDocuments(results, images, file_id)

    if mlFile.allSorted:
        json = convert_to_json(mlFile)
        print("json: {}".format(json))
        return json

    return None
