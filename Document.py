from datetime import date
import json

class MLDocument:
    def __init__(
        self, className: str, pages: list[int], dateOnly: date
    ):
        self.className: str = className
        self.pages: list[int] = pages
        self.date: str = dateOnly.isoformat()

class MLFile:
    def __init__(self, id: str ,documents: list[MLDocument] = [], allSorted: bool = False):
        self.id = id
        self.allSorted = allSorted
        self.documents = documents
        self.type: int = 4
        
class MyCustomDocumentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MLDocument):
            return {
                "className": obj.className,
                "pages": str(obj.pages),
                "date": obj.date,
            }
            
            
class MyCustomFileEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MLFile):
            return {
                'id': obj.id,
                'allSorted': str(obj.allSorted),
                'documents': json.dumps(obj.documents, cls=MyCustomDocumentEncoder),
                'type': obj.type
            }