import re

from models.LayoutRegex import (
    Coordinate,
    DateRegex,
    ExtractAmount,
    ExtractDate,
    ExtractPageNumber,
    Layout,
    PageRegex,
)
from models.MyRegex import MyRegex


page_of_total = PageRegex(r"(\d+)\s*(of|Of|0f|oF|OF|0F)\s*(\d+)", 1, 3)
page_number = PageRegex(r"(\d+)", 1, 0)


def build_mmm_dd_yy(general_position: int):
    return DateRegex(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{2})",
        general_position,
        2,
        1,
        3,
    )


def build_mmm_dd_yyyy(general_position: int):
    return DateRegex(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
        general_position,
        2,
        1,
        3,
    )


def build_mmmm_dd_yyyy(general_position: int):
    return DateRegex(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
        general_position,
        2,
        1,
        3,
    )


def build_mmm_dd_yyyy(general_position: int):
    return DateRegex(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\D+(\d{1,2})\D+(\d{4})",
        general_position,
        2,
        1,
        3,
    )


def build_mm_dd_yyyy(general_position: int):
    return DateRegex(r"(\d{1,2})/(\d\d)/(\d{4})", general_position, 2, 1, 3)


def build_mm_dd_yy(general_position: int):
    return DateRegex(r"(\d\d)/(\d\d)/(\d\d)", general_position, 2, 1, 3)


mb_cu_date_coordinate = ExtractDate(
    1,
    build_mmm_dd_yyyy(2),
    0.02734375,
    0.048828125,
    0.59375,
    0.119140625,
)

mb_cu_page_coordinate = ExtractPageNumber(
    1, page_of_total, 0.787109375, 0.884765625, 0.1796875, 0.099609375
)

layouts = [
    Layout(
        "TD Bank",
        [
            ExtractPageNumber(
                1,
                page_of_total,
                0.6698039215686274,
                0.3496969696969697,
                0.23215686274509803,
                0.02303030303030303,
            ),
            ExtractPageNumber(
                2,
                page_of_total,
                0.792156862745098,
                0.06424242424242424,
                0.19215686274509805,
                0.04181818181818182,
            ),
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yy(1),
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
            ExtractPageNumber(
                1,
                page_of_total,
                0.054901960784313725,
                0.8957575757575758,
                0.19294117647058823,
                0.052121212121212124,
            )
        ],
        [
            ExtractDate(
                1,
                build_mmmm_dd_yyyy(1),
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
            ExtractPageNumber(
                1,
                page_of_total,
                0.8094117647058824,
                0.9503030303030303,
                0.1592156862745098,
                0.03939393939393939,
            )
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yy(1),
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
            ExtractPageNumber(
                1, page_of_total, 0.822265625, 0.8203125, 0.171875, 0.17578125
            ),
            ExtractPageNumber(
                1,
                page_of_total,
                0.876078431372549,
                0.8818181818181818,
                0.1403921568627451,
                0.026060606060606062,
            ),
        ],
        [
            ExtractDate(
                1,
                build_mmmm_dd_yyyy(2),
                0.596078431372549,
                0.13333333333333333,
                0.396078431372549,
                0.044848484848484846,
            ),
            ExtractDate(
                1,
                build_mmmm_dd_yyyy(2),
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
            ExtractPageNumber(
                1,
                page_of_total,
                0.8862745098039215,
                0.9218181818181819,
                0.1003921568627451,
                0.044848484848484846,
            )
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yy(1),
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
            ExtractPageNumber(
                1,
                page_of_total,
                0.5121568627450981,
                0.15212121212121213,
                0.06588235294117648,
                0.02303030303030303,
            )
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yy(1),
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
            ExtractPageNumber(
                1, page_of_total, 0.486328125, 0.15625, 0.08984375, 0.025390625
            ),
            ExtractPageNumber(
                1,
                page_of_total,
                0.2196078431372549,
                0.004242424242424243,
                0.6149019607843137,
                0.04787878787878788,
            ),
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yy(1),
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
            ExtractPageNumber(
                1,
                page_of_total,
                0.876078431372549,
                0.052121212121212124,
                0.09333333333333334,
                0.01575757575757576,
            ),
            ExtractPageNumber(
                1,
                page_of_total,
                0.832156862745098,
                0.052121212121212124,
                0.06352941176470588,
                0.017575757575757574,
            ),
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yy(1),
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
            ExtractPageNumber(
                1, page_of_total, 0.859375, 0.689453125, 0.14453125, 0.064453125
            ),
            ExtractPageNumber(
                1,
                page_of_total,
                0.8286384976525821,
                0.6315151515151515,
                0.17136150234741784,
                0.12606060606060607,
            ),
            ExtractPageNumber(
                1,
                page_of_total,
                0.8649921507064364,
                0.9643734643734644,
                0.12637362637362637,
                0.03194103194103194,
            ),
        ],
        [
            ExtractDate(
                1,
                build_mm_dd_yy(2),
                0.708984375,
                0.09375,
                0.283203125,
                0.18359375,
            )
        ],
    ),
    Layout(
        "Big Freight",
        [
            ExtractPageNumber(
                1, page_of_total, 0.826171875, 0.86328125, 0.1640625, 0.125
            ),
            ExtractPageNumber(
                1, page_of_total, 0.0, 0.728515625, 0.12109375, 0.26171875
            ),
        ],
        [
            ExtractDate(
                1,
                DateRegex(
                    r"Pay\D+Period\D{1,2}(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3
                ),
                0.33203125,
                0.0234375,
                0.419921875,
                0.119140625,
            ),
            ExtractDate(
                1,
                DateRegex(
                    r"Pay\D+Period\D{1,2}(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3
                ),
                0.89453125,
                0.31640625,
                0.103515625,
                0.349609375,
            ),
        ],
    ),
    Layout(
        "TransX",
        [
            ExtractPageNumber(1, page_number, 0.296875, 0.92, 0.32421875, 0.12109375),
        ],
        [
            ExtractDate(
                1,
                DateRegex(r"(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3),
                0.5859375,
                0.0,
                0.412109375,
                0.134765625,
            )
        ],
    ),
    Layout(
        "DeckX",
        [
            ExtractPageNumber(1, page_number, 0.296875, 0.92, 0.32421875, 0.12109375),
        ],
        [
            ExtractDate(
                1,
                DateRegex(r"(\d{1,2})/(\d{1,2})/(\d\d\d\d)", 1, 2, 1, 3),
                0.5859375,
                0.0,
                0.412109375,
                0.134765625,
            )
        ],
    ),
    Layout(
        "Rogers",
        [
            ExtractPageNumber(
                1, page_of_total, 0.302734375, 0.0078125, 0.400390625, 0.0859375
            )
        ],
        [
            ExtractDate(
                1,
                build_mmm_dd_yyyy(1),
                0.18359375,
                0.015625,
                0.509765625,
                0.08203125,
            )
        ],
        [
            ExtractAmount(
                Coordinate(1, 0.50390625, 0.259765625, 0.5625, 0.240234375),
                [
                    MyRegex(re.compile(r"total.*total"), 1),
                    MyRegex(re.compile(r"(\d*,?\d+\.\d{2}|\d+)"), -2),
                ],
            )
        ],
    ),
    Layout(
        "Telus",
        [
            ExtractPageNumber(
                1, page_of_total, 0.8359375, 0.55859375, 0.158203125, 0.19921875
            ),
            ExtractPageNumber(
                1, page_of_total, 0.712890625, 0.8671875, 0.28125, 0.12890625
            ),
        ],
        [
            ExtractDate(
                1, build_mmmm_dd_yyyy(1), 0.1953125, 0.00390625, 0.32421875, 0.087890625
            )
        ],
        [
            ExtractAmount(
                Coordinate(1, 0.044921875, 0.255859375, 0.580078125, 0.322265625),
                [
                    MyRegex(re.compile(r"Total.*Total"), 1),
                    MyRegex(re.compile(r"(\d+\.\d{2})"), 1),
                ],
            )
        ],
    ),
    Layout(
        "Bell Mobility",
        [
            ExtractPageNumber(
                1,
                PageRegex(r"(\d+)(\D+/\D+)(\d+)", 1, 3),
                0.78515625,
                0.0234375,
                0.20703125,
                0.140625,
            ),
        ],
        [
            ExtractDate(
                1, build_mmmm_dd_yyyy(1), 0.78515625, 0.0234375, 0.20703125, 0.140625
            )
        ],
        [
            ExtractAmount(
                Coordinate(1, 0.107421875, 0.1796875, 0.595703125, 0.38671875),
                [
                    MyRegex(re.compile(r"Total\s+current\D+\d+\.\d{2}"), 1),
                    MyRegex(re.compile(r"(\d+\.\d{2})"), 1),
                ],
            )
        ],
    ),
    Layout(
        "Bell",
        [
            ExtractPageNumber(
                1, page_of_total, 0.771484375, 0.00390625, 0.22265625, 0.05078125
            ),
        ],
        [
            ExtractDate(
                1, build_mmmm_dd_yyyy(1), 0.66015625, 0.09765625, 0.337890625, 0.140625
            )
        ],
        [
            ExtractAmount(
                Coordinate(1, 0.0078125, 0.16015625, 0.671875, 0.1484375),
                [
                    MyRegex(re.compile(r"New\s+Charges\D+\d+\.\d{2}"), 1),
                    MyRegex(re.compile(r"(\d+\.\d{2})"), 1),
                ],
            )
        ],
    ),
    Layout(
        "Bison",
        [
            ExtractPageNumber(
                1,
                PageRegex(r"(\d+)(\D?/\D?)(\d+)", 1, 3),
                0.345703125,
                0.91796875,
                0.28125,
                0.078125,
            ),
        ],
        [
            ExtractDate(
                1, build_mmm_dd_yyyy(1), 0.712890625, 0.046875, 0.279296875, 0.08203125
            )
        ],
        [],
    ),
    Layout(
        "Steves Livestock",
        [
            ExtractPageNumber(
                1,
                PageRegex(r"Page\D+(\d{1,2})", 1, -1),
                0.296875,
                0.947265625,
                0.341796875,
                0.046875,
            ),
        ],
        [
            ExtractDate(
                1, build_mm_dd_yyyy(2), 0.5625, 0.009765625, 0.435546875, 0.1328125
            )
        ],
        [],
    ),
]


def getLayout(className: str):
    for l in layouts:
        if l.className == className:
            return l

    return None
