from models.MyRegex import MyRegex


class PageRegex:
    def __init__(self, generalRegex, pagePosition: int, pageOfPosition: int):
        self.generalRegex = generalRegex
        self.pagePosition: int = pagePosition
        self.pageOfPosition: int = pageOfPosition


class DateRegex:
    def __init__(
        self,
        generalRegex,
        generalPosition: int,
        dayPosition: int,
        monthPosition: int,
        yearPosition: int,
    ):
        self.generalRegex = generalRegex
        self.dayPosition: int = dayPosition
        self.monthPosition: int = monthPosition
        self.yearPosition: int = yearPosition
        self.generalPosition: int = generalPosition


class Coordinate:
    def __init__(self, pageNumber: int, x: float, y: float, w: float, h: float):
        self.pageNumber: int = pageNumber
        self.x: int = x
        self.y: int = y
        self.w: int = w
        self.h: int = h


class ExtractPageNumber:
    def __init__(
        self, pageNumber: int, regex: PageRegex, x: float, y: float, w: float, h: float
    ):
        self.coordinate: Coordinate = Coordinate(pageNumber, x, y, w, h)
        self.regex: PageRegex = regex


class ExtractDate:
    def __init__(
        self, pageNumber: int, regex: DateRegex, x: float, y: float, w: float, h: float
    ):
        self.coordinate: Coordinate = Coordinate(pageNumber, x, y, w, h)
        self.regex: DateRegex = regex


class ExtractAmount:
    def __init__(self, coordinates: Coordinate, myRegex: list[MyRegex]):
        self.coordinates: Coordinate = coordinates
        self.amountRegex: list[MyRegex] = myRegex


class Layout:
    def __init__(
        self,
        class_name: str,
        pageNumber: list[ExtractPageNumber],
        date: list[ExtractDate],
        amount: list[ExtractAmount] = [],
    ):
        self.className: str = class_name
        self.pageNumber: list[ExtractPageNumber] = pageNumber
        self.date: list[ExtractDate] = date
        self.amount: list[ExtractAmount] = amount
