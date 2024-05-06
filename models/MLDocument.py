from datetime import date
import json


class MLDocument:
    def __init__(self, className: str, pages: list[int], dateOnly: date):
        self.className: str = className
        self.pages: list[int] = pages
        self.date: str = dateOnly.isoformat()


class MyCustomDocumentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MLDocument):
            return {
                "className": obj.className,
                "pages": str(obj.pages),
                "date": obj.date,
            }
