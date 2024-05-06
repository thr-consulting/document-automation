import json
from models.MLDocument import MLDocument, MyCustomDocumentEncoder


class MLFile:
    def __init__(
        self, id: str, documents: list[MLDocument] = [], allSorted: bool = False
    ):
        self.id = id
        self.allSorted = allSorted
        self.documents = documents
        self.type: int = 4


class MyCustomFileEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MLFile):
            return {
                "id": obj.id,
                "allSorted": str(obj.allSorted),
                "documents": json.dumps(obj.documents, cls=MyCustomDocumentEncoder),
                "type": obj.type,
            }
