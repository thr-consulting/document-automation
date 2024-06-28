import json
from models.MLDocument import MLDocument

class MLFile:
    def __init__(
        self, id: str, documents: list[MLDocument] = [], allSorted: bool = False
    ):
        self.id: str = id
        self.allSorted: bool = allSorted
        self.documents: list[MLDocument] = documents
        self.type: int = 4

class MyCustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MLFile):
            return obj.__dict__
        elif isinstance(obj, MLDocument):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def convert_to_json(data):
    return json.dumps(data, cls=MyCustomEncoder)