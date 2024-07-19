from extract.date import extractDate
from extract.amount import extractAmount
from models.MLFile import MLFile
from models.MLDocument import MLDocument
from models.PageResult import PageResult


def isSinglePageValleyFiber(pageResults: list[PageResult]) -> bool:
    result = len(pageResults) == 1 and pageResults[0].className == "Valley Fiber"
    print(f"single page is valley fiber: {result}")
    return result

def isFirstPageMBHydro(pageResults: list[PageResult]) -> bool:
    result = len(pageResults) and pageResults[0].className == "MB Hydro"
    print(f"first page is MB Hydro: {result}")
    return result

def isFirstPageWpgWWDepartment(pageResults: list[PageResult]) -> bool:
    result = len(pageResults) and pageResults[0].className == "Wpg Water Waste Department"
    print(f"first page is Wpg Water Waste Department: {result}")
    return result


def allIncrement(pageResults: list[PageResult]) -> bool:
    if len(pageResults) == 1:
        return pageResults[0].predictedPageNum == 1

    for i in range(1, len(pageResults)):
        if int(pageResults[i].predictedPageNum) != (
            1 + int(pageResults[i - 1].predictedPageNum)
        ):
            return False

    return True


def allIncrementWhenSorted(pageResults: list[PageResult]) -> bool:
    pageResults = sorted(pageResults, key=lambda page: page.predictedPageNum)
    return allIncrement(pageResults)


def allIncrementLastPageEmpty(pageResults: list[PageResult]) -> bool:
    if len(pageResults) == 1:
        return pageResults[0].predictedPageNum == 1

    # don't check last page
    for i in range(1, len(pageResults) - 1):
        if int(pageResults[i].predictedPageNum) != (
            1 + int(pageResults[i - 1].predictedPageNum)
        ):
            return False

    # make sure last page is "Empty Page"
    return pageResults[len(pageResults) - 1].className == "Empty Page"


def allSameVendor(pageResults: list[PageResult]) -> bool:
    if len(pageResults) == 1:
        return True

    for i in range(1, len(pageResults)):
        if pageResults[i].className != pageResults[i - 1].className:
            return False

    return True


def createDocuments(pageResults: list[PageResult], images, fileId: str) -> MLFile:
    print("creating documents...")
    file: MLFile = MLFile(fileId)
    file.documents = []

    if isSinglePageValleyFiber(pageResults):
        VALLEY_FIBER = "Valley Fiber"

        if len(pageResults) == 1:
            date = extractDate(VALLEY_FIBER, images)
            if date:
                amount = extractAmount(VALLEY_FIBER, images)

                file.documents.append(
                    MLDocument(
                        pageResults[0].className,
                        list(range(1, len(pageResults) + 1)),
                        date,
                        amount,
                    )
                )

                file.allSorted = True
                file.partialSort = True       
    elif isFirstPageMBHydro(pageResults):
        MB_HYDRO = "MB Hydro"

        if len(pageResults) == 1:
            date = extractDate(MB_HYDRO, images)
            if date:
                amount = extractAmount(MB_HYDRO, images)

                file.documents.append(
                    MLDocument(
                        pageResults[0].className,
                        list(range(1, len(pageResults) + 1)),
                        date,
                        amount,
                    )
                )

                file.allSorted = True
                file.partialSort = True

    elif isFirstPageWpgWWDepartment(pageResults):
        WPG_WW_Department = "Wpg Water Waste Department"

        if len(pageResults) == 1:
            date = extractDate(WPG_WW_Department, images)
            if date:
                amount = extractAmount(WPG_WW_Department, images)

                file.documents.append(
                    MLDocument(
                        pageResults[0].className,
                        list(range(1, len(pageResults) + 1)),
                        date,
                        amount,
                    )
                )

                file.allSorted = True
                file.partialSort = True

    elif allIncrement(pageResults):
        print("all pages are incrementing - no exceptions")

        # extract date
        date = extractDate(pageResults[0].className, images)
        if date:
            amount = extractAmount(pageResults[0].className, images)
            file.documents.append(
                MLDocument(
                    pageResults[0].className,
                    list(range(1, len(pageResults) + 1)),
                    date,
                    amount,
                )
            )

            file.allSorted = True
            file.partialSort = False

    elif allIncrementWhenSorted(pageResults):
        print("all pages are incrementing - when sorted by page numbers")

        # extract date
        date = extractDate(pageResults[0].className, images)
        if date:
            amount = extractAmount(pageResults[0].className, images)
            file.documents.append(
                MLDocument(
                    pageResults[0].className,
                    list(range(1, len(pageResults) + 1)),
                    date,
                    amount,
                )
            )

            file.allSorted = True
            file.partialSort = False

    elif allIncrementLastPageEmpty(pageResults):
        print("all pages are incrementing - except last page predicted empty")

        # extract date
        date = extractDate(pageResults[0].className, images)
        if date:
            amount = extractAmount(pageResults[0].className, images)
            file.documents.append(
                MLDocument(
                    pageResults[0].className,
                    list(range(1, len(pageResults) + 1)),
                    date,
                    amount,
                )
            )

            file.allSorted = True
            file.partialSort = True

    print("\n---\nfile id: {}".format(file.id))
    print(
        f"\n---\nall pages sorted: {file.allSorted}\npartial sorting: {file.partialSort}\n---"
    )
    for i in file.documents:
        print(i.className, i.date, i.pages)

    return file
