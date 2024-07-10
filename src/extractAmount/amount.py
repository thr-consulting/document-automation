from typing import Pattern
import re

from data.layouts import Layout, getLayout
from ocr.extract import extractText


class MyRegex:
    def __init__(self, groupRegex: Pattern, extractPosition: int):
        self.groupRegex = groupRegex
        self.extractPosition = extractPosition

# -2 implies get last match
def txtToAmount(text: str, regex: list[MyRegex]):
    txt = text

    for r in regex:
        print(r.groupRegex.pattern)
        match = re.findall(r.groupRegex.pattern, txt, flags=re.DOTALL | re.IGNORECASE)
        if len(match) == 0:
            print(f"-no matches found for pattern: {r.groupRegex.pattern}")
            print(f"-text: {txt}")
            return None
        elif r.extractPosition == -2:
            txt = match[len(match) - 1]
        else:
            txt = match[r.extractPosition - 1]
        print(txt)

    return float(txt.replace(',',''))

def extractAmount(className: str, images) -> float | None:
    print("\namount to text...")

    # get layout
    layout: Layout = getLayout(className)
    if layout == None or len(layout.amount) == 0:
        return None
    
    extractedAmount = extractText(images[0], layout.amount[0].coordinates)
    return txtToAmount(extractedAmount, layout.amount[0].amountRegex)