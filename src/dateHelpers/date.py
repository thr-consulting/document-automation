from datetime import date
import re
from data.layouts import DateRegex, Layout, getLayout
from ocr.extract import extractText


def txtToDay(general: str, regex: DateRegex) -> int:
    return int(general[regex.dayPosition - 1])


def txtToMonth(general: str, regex: DateRegex) -> int:
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
    monthLength = len(general[regex.monthPosition - 1])
    print("month length: {}".format(monthLength))

    if monthLength == 1 or monthLength == 2:
        return int(general[regex.monthPosition - 1])
    else:
        return months.index(general[regex.monthPosition - 1].lower()) + 1


def txtToYear(general: str, regex: DateRegex) -> int:
    extracted_year = int(general[regex.yearPosition - 1])
    if extracted_year < 2000:
        extracted_year = extracted_year + 2000

    return extracted_year


def txtToDate(txt: str, regex: DateRegex) -> date:
    general = re.findall(regex.generalRegex, txt, flags=re.IGNORECASE)
    print(general)

    if len(general) >= regex.generalPosition:
        general = general[regex.generalPosition - 1]
        print("general match: {}".format(general))

        extracted_day = txtToDay(general, regex)
        extracted_month = txtToMonth(general, regex)
        extracted_year = txtToYear(general, regex)

        extracted_date = date(
            extracted_year, extracted_month, extracted_day
        )

        print(f"date: {extracted_date.isoformat()}")
        return extracted_date

    print("no general match for date regex")
    return None


def extractDate(className: str, images) -> date:
    print("\nextracting date...")

    # get layout
    layout: Layout = getLayout(className)
    if layout:
        print("FOUND layout for className: {}".format(className))
        # get which page to extract date from
        page = layout.date[0].pageNumber

        # get date text
        for currLayout in layout.date:
            print(f"trying layout: {currLayout.pageNumber}, {currLayout.regex.generalRegex}, {currLayout.x}, {currLayout.y}, {currLayout.h}, {currLayout.w}")
            txt = extractText(images[page - 1], currLayout)

            # get actual date with regex
            date = txtToDate(txt, currLayout.regex)

            if date:
                print(f"found date: {date}")
                return date
        
        return None
    else:
        print("FAILED to find layout for className: {}".format(className))
        return None
