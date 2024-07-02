import os
import json
import torch

from documentBuilder.build import createDocuments
from images.pdf2jpg import pdf2JpgFromURL
from models.MLFile import convert_to_json
from pageNumberHelpers.extractPageNumber import assignPageNumbers
from pytorch import load_model, predict_images
from dotenv import load_dotenv

load_dotenv() 

os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # run on cpu

MODEL_PATH = os.environ["MODEL_PATH"]
MODEL_IMAGE_SIZE = int(os.environ["MODEL_IMAGE_SIZE"])
MODEL_CLASSES_PATH = os.environ["MODEL_CLASSES_PATH"]

print(f"pytorch version: {torch.__version__}\n")
# classes
classes = json.load(open(MODEL_CLASSES_PATH))
print(f"{len(classes)} classes")

# load model
device = torch.device("cpu")
model, transform = load_model(MODEL_PATH, classes, MODEL_IMAGE_SIZE, device)


def workflow(pdf_path, file_id: str = "file_id"):
    images = pdf2JpgFromURL(pdf_path)

    if len(images) > 5:
        print("more than 5 images... skip processing")
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
