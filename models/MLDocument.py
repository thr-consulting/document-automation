from datetime import date

class MLDocument:
    def __init__(self, className: str, pages: list[int], dateOnly: date):
        self.className: str = className
        self.pages: list[int] = pages
        self.date: str = dateOnly.isoformat()
