from datetime import date
import re
from data.layouts import DateRegex, Layout, getLayout
from ocr.extract import extractText


def getRegexDate(txt: str, regex: DateRegex) -> date:
    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]
    general = re.findall(regex.general_regex, txt, flags=re.IGNORECASE)
    print(general)
    if len(general) >= regex.generalPosition:
        general = general[regex.generalPosition - 1]
        print("general match: {}".format(general))

        extracted_day = int(general[regex.dayPosition - 1])
        
        monthLength = len(general[regex.monthPosition - 1])
        print("month length: {}".format(monthLength))
        if monthLength == 1 or monthLength == 2:
            extracted_month = int(general[regex.monthPosition - 1])
        else:
            extracted_month = months.index(general[regex.monthPosition - 1].lower()) + 1
            
        extracted_year = int(general[regex.yearPosition - 1])
        if extracted_year < 2000:
            extracted_year = extracted_year + 2000
            
        print(
            "date: {}".format(
                date(extracted_year, extracted_month, extracted_day).isoformat()
            )
        )

        return date(extracted_year, extracted_month, extracted_day)
    print("no general match for date regex")
    return None


def extractDate(className: str, images) -> date:
    print("extracting date...")

    # get layout
    layout: Layout = getLayout(className)
    if layout:
        print("FOUND layout for className: {}".format(className))
        # get which page to extract date from
        page = layout.date[0].pageNumber

        # get date text
        txt = extractText(images[page - 1], layout.date[0])

        # get actual date with regex
        date = getRegexDate(txt, layout.date[0].regex)

        return date
    else:
        print("FAILED to find layout for className: {}".format(className))
        return None
