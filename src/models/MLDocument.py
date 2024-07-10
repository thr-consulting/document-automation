from datetime import date

class MLDocument:
    def __init__(self, className: str, pages: list[int], dateOnly: date, amount: float | None = None):
        self.className: str = className
        self.pages: list[int] = pages
        self.date: str = dateOnly.isoformat()
        self.amount: float | None = amount 
