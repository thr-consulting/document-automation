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


class PageCoordinate(Coordinate):
    def __init__(
        self, pageNumber: int, regex: PageRegex, x: float, y: float, w: float, h: float
    ):
        super().__init__(pageNumber, x, y, w, h)
        self.regex = regex


class DateCoordinate(Coordinate):
    def __init__(
        self, pageNumber: int, regex: DateRegex, x: float, y: float, w: float, h: float
    ):
        super().__init__(pageNumber, x, y, w, h)
        self.regex = regex


class Layout:
    def __init__(
        self,
        class_name: str,
        pageNumber: list[PageCoordinate],
        date: list[DateCoordinate],
    ):
        self.className: str = class_name
        self.pageNumber: list[PageCoordinate] = pageNumber
        self.date: list[DateCoordinate] = date


page_of_total = PageRegex(r"(\d+)\s*(of|Of|0f|oF|OF|0F)\s*(\d+)", 1, 3)
page_number = PageRegex(r"(\d+)", 1, 0)
mmmm_dd_yyyy = DateRegex(
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
    2,
    2,
    1,
    3,
)
mmm_dd_yyyy = DateRegex(
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
    2,
    2,
    1,
    3,
)

mmm_dd_yy = DateRegex(
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{2})",
    2,
    2,
    1,
    3,
)


mb_cu_date_coordinate = DateCoordinate(
    1,
    mmmm_dd_yyyy,
    0.02734375,
    0.048828125,
    0.59375,
    0.119140625,
)

mb_cu_page_coordinate = PageCoordinate(
    1, page_of_total, 0.787109375, 0.884765625, 0.1796875, 0.099609375
)

layouts = [
    Layout(
        "TD Bank",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.6698039215686274,
                0.3496969696969697,
                0.23215686274509803,
                0.02303030303030303,
            ),
            PageCoordinate(
                2,
                page_of_total,
                0.792156862745098,
                0.06424242424242424,
                0.19215686274509805,
                0.04181818181818182,
            ),
        ],
        [
            DateCoordinate(
                1,
                mmm_dd_yy,
                0.6698039215686274,
                0.32,
                0.23294117647058823,
                0.02303030303030303,
            )
        ],
    ),
    Layout(
        "BMO Bank",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.054901960784313725,
                0.8957575757575758,
                0.19294117647058823,
                0.052121212121212124,
            )
        ],
        [
            DateCoordinate(
                1,
                DateRegex(
                    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
                    1,
                    2,
                    1,
                    3,
                ),
                0.08941176470588236,
                0.32727272727272727,
                0.5207843137254902,
                0.045454545454545456,
            )
        ],
    ),
    Layout(
        "CIBC Bank",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.8094117647058824,
                0.9503030303030303,
                0.1592156862745098,
                0.03939393939393939,
            )
        ],
        [
            DateCoordinate(
                1,
                DateRegex(
                    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
                    1,
                    2,
                    1,
                    3,
                ),
                0.6376470588235295,
                0.18363636363636363,
                0.28941176470588237,
                0.03333333333333333,
            )
        ],
    ),
    Layout(
        "RBC Bank",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.9003921568627451,
                0.8703030303030304,
                0.08941176470588236,
                0.0503030303030303,
            ),
            PageCoordinate(
                1,
                page_of_total,
                0.876078431372549,
                0.8818181818181818,
                0.1403921568627451,
                0.026060606060606062,
            ),
        ],
        [
            DateCoordinate(
                1,
                mmmm_dd_yyyy,
                0.596078431372549,
                0.13333333333333333,
                0.396078431372549,
                0.044848484848484846,
            ),
            DateCoordinate(
                1,
                mmmm_dd_yyyy,
                0.6392156862745098,
                0.1315151515151515,
                0.4337254901960784,
                0.022424242424242423,
            ),
        ],
    ),
    Layout(
        "Scotia Bank",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.8862745098039215,
                0.9218181818181819,
                0.1003921568627451,
                0.044848484848484846,
            )
        ],
        [
            DateCoordinate(
                1,
                DateRegex(
                    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
                    1,
                    2,
                    1,
                    3,
                ),
                0.72,
                0.19575757575757577,
                0.17411764705882352,
                0.03393939393939394,
            )
        ],
    ),
    Layout(
        "RBC Credit",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.5121568627450981,
                0.15212121212121213,
                0.06588235294117648,
                0.02303030303030303,
            )
        ],
        [
            DateCoordinate(
                1,
                DateRegex(
                    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
                    1,
                    2,
                    1,
                    3,
                ),
                0.07764705882352942,
                0.1193939393939394,
                0.40941176470588236,
                0.05333333333333334,
            )
        ],
    ),
    Layout(
        "TD Credit",
        [
            PageCoordinate(
                1, page_of_total, 0.486328125, 0.15625, 0.08984375, 0.025390625
            ),
            PageCoordinate(
                1,
                page_of_total,
                0.2196078431372549,
                0.004242424242424243,
                0.6149019607843137,
                0.04787878787878788,
            ),
        ],
        [
            DateCoordinate(
                1,
                DateRegex(
                    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
                    1,
                    2,
                    1,
                    3,
                ),
                0.046875,
                0.15625,
                0.466796875,
                0.021484375,
            )
        ],
    ),
    Layout(
        "Scotia Credit",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.876078431372549,
                0.052121212121212124,
                0.09333333333333334,
                0.01575757575757576,
            ),
            PageCoordinate(
                1,
                page_of_total,
                0.832156862745098,
                0.052121212121212124,
                0.06352941176470588,
                0.017575757575757574,
            ),
        ],
        [
            DateCoordinate(
                1,
                DateRegex(
                    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
                    1,
                    2,
                    1,
                    3,
                ),
                0.7584313725490196,
                0.02727272727272727,
                0.2384313725490196,
                0.012727272727272728,
            )
        ],
    ),
    Layout(
        "SCU Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "RCU Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "Access Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "Assiniboine Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "Stride Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "Niverville Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "Sunrise Bank",
        [mb_cu_page_coordinate],
        [mb_cu_date_coordinate],
    ),
    Layout(
        "MBNA Credit",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.8818466353677621,
                0.7103030303030303,
                0.11189358372456965,
                0.019393939393939394,
            ),
            PageCoordinate(
                1,
                page_of_total,
                0.8649921507064364,
                0.9643734643734644,
                0.12637362637362637,
                0.03194103194103194,
            ),
        ],
        [
            DateCoordinate(
                1,
                DateRegex(r"(\d\d)/(\d\d)/(\d\d)", 2, 2, 1, 3),
                0.690923317683881,
                0.15878787878787878,
                0.28012519561815336,
                0.04727272727272727,
            )
        ],
    ),
    Layout(
        "Big Freight",
        [
            PageCoordinate(
                1,
                page_of_total,
                0.826171875, 0.86328125, 0.1640625, 0.125
            ),
            PageCoordinate(
                1,
                page_of_total,
                0.0, 0.728515625, 0.12109375, 0.26171875
            ),
        ],
        [
            DateCoordinate(
                1,
                DateRegex(r"Pay\D+Period\D{1,2}(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3),
                0.33203125, 0.0234375, 0.419921875, 0.119140625
            ),
            DateCoordinate(
                1,
                DateRegex(r"Pay\D+Period\D{1,2}(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3),
                0.89453125, 0.31640625, 0.103515625, 0.349609375
            )
        ],
    ),
    Layout(
        "TransX",
        [
            PageCoordinate(
                1,
                page_number,
                0.38176470588235295,
                0.9063636363636364,
                0.21176470588235294,
                0.04863636363636364,
            ),
        ],
        [
            DateCoordinate(
                1,
                DateRegex(r"(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3),
                0.6447058823529411,
                0.028181818181818183,
                0.2811764705882353,
                0.015454545454545455,
            )
        ],
    ),
    Layout(
        "DeckX",
        [
            PageCoordinate(
                1,
                page_number,
                0.38176470588235295,
                0.9063636363636364,
                0.21176470588235294,
                0.04863636363636364,
            ),
        ],
        [
            DateCoordinate(
                1,
                DateRegex(r"(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3),
                0.6447058823529411,
                0.028181818181818183,
                0.2811764705882353,
                0.015454545454545455,
            )
        ],
    ),
    Layout(
        "Rogers",
        [PageCoordinate(1, page_of_total, 0.302734375, 0.0078125, 0.400390625, 0.0859375)],
        [DateCoordinate(1, mmm_dd_yyyy, 0.18359375, 0.015625, 0.509765625, 0.08203125)]
        )
]


def getLayout(className: str):
    for l in layouts:
        if l.className == className:
            return l

    return None
