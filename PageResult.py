class PageResult:
    def __init__(self, originalOrder: int, className: str, predictScore: float):
        self.originalOrder: int = originalOrder
        self.className: str = className
        self.predictScore: float = predictScore
        self.predictedPageNum: int = -1
        self.predictedPageNumOf: int = -1