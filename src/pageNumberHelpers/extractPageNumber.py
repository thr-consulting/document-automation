import re

from data.layouts import PageRegex, getLayout
from models.PageResult import PageResult
from ocr.extract import extractText


def processPageRegex(pageRegex: PageRegex, txt):
    if len(txt) > 0:
        general = re.findall(pageRegex.general, txt)
        if len(general):
            general = general[0]
            print("general page: {}".format(general))
            if pageRegex.pageOfPosition == 0:
                # total pages does not exist
                return (int(general[pageRegex.pagePosition - 1]), -1) 
            else:
                # get both page number and total pages
                return (
                int(general[pageRegex.pagePosition - 1]),
                (
                    general[pageRegex.pageOfPosition - 1]
                    if pageRegex.pageOfPosition > 0
                    else -1
                ),
            )

    return (-1, -1)


# assign page number to a single page
def assignVendorPageNumber(page: PageResult, image, className: str):
    # get layout
    layout = getLayout(className)

    # get page num text
    if layout:
        for l in layout.pageNumber:
            txt = extractText(image, l)

            # get actual page number
            if len(txt) > 0:
                p_num, p_of = processPageRegex(l.regex, txt)

                page.predictedPageNum = p_num
                page.predictedPageNumOf = p_of

                # break once page number is found
                if p_num != -1:
                    break


# assign page numbers to all pages
def assignPageNumbers(results: list[PageResult], images):
    assert len(results) > 0
    print(f"\nassign {str(len(results))} page numbers")
    for p in range(len(results)):
        # step 1: assume page 2 or greater is the same className as the previous page, so use previous class layout
        if p > 0:
            assignVendorPageNumber(results[p], images[p], results[p - 1].className)
        else:
            assignVendorPageNumber(results[p], images[p], results[p].className)

        # if current page number is valid then current className is same as previous className
        if results[p].predictedPageNum > 1:
            results[p].className = results[p - 1].className
            results[p].predictScore = 0

        # step 2: current page is different than previous page
    
    for result in results:
        print("{} -- {} -- {}".format(result.className, result.predictScore, result.predictedPageNum))
    print("-------------\n")
