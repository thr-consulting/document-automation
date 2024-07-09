from dateHelpers.date import extractDate
from models.MLFile import MLFile
from models.MLDocument import MLDocument
from models.PageResult import PageResult


def allIncrement(results: list[PageResult]) -> bool:
    if len(results) == 1:
        return results[0].predictedPageNum == 1

    for i in range(1, len(results)):
        if int(results[i].predictedPageNum) != (
            1 + int(results[i - 1].predictedPageNum)
        ):
            return False

    return True


# # assumes page numbers start at 1 and are only missing in the middle
# def singlePageWithNoPageNumberInMiddle(results: list[PageResult]) -> bool:
#     if len(results) == 0:
#         return False

#     if len(results) == 1:
#         # no page missing if page_number == 1
#         return results[0].predictedPageNum != 1

#     numPagesMissing = 0  # assume no page missing to start

#     for i in len(results):
#         if i > 1:
#             if (
                # results[i - 2].predictedPageNum + 1 ????= results[i].predictedPageNum
#                 and results[i - 1].predictedPageNum == -1
#             ):
#                 print(f"page missing: {results[i].predictedPageNum - 1 }")
#                 numPagesMissing += 1

#     return numPagesMissing == 1


# def allIncrementingPagesExceptLastHasNoPageNumber(results: list[PageResult]) -> bool:
#     assert len(results) > 1

#     allIncrementExceptLast = True
#     for i in len(results):
#         if i == len(results) - 1:
#             allIncrementExceptLast = results[i].predictedPageNum == -1
#             break
#         if i > 0:
#             if results[i - 1].predictedPageNum + 1 != results[i].predictedPageNum:
#                 allIncrementExceptLast = False
#                 break

#     return allIncrementExceptLast


def allSameVendor(results: list[PageResult]) -> bool:
    if len(results) == 1:
        return True

    for i in range(1, len(results)):
        if results[i].className != results[i - 1].className:
            return False

    return True


def createDocuments(results: list[PageResult], images, fileId: str) -> MLFile:
    print("creating documents...")
    file: MLFile = MLFile(fileId)
    file.documents = []


    if allIncrement(results):
        # pdf file == [incrementing page numbers with no exception - doesn't have to start at 1]
        print("all pages are incrementing - no pages are missing")

        # extract date
        date = extractDate(results[0].className, images)
        if date:
            file.documents.append(
                MLDocument(
                    results[0].className,
                    list(range(1, len(results) + 1)),
                    date,
                )
            )
            file.allSorted = True

    # # pdf file == 1 vendor with no pages missing
    # elif noPageMissing(results):
    #     print("pdf pages all have same vendor, with no pages missing")

    #     # extract date
    #     date = extractDate(results[0].className, images)

    #     # get all valid pages
    #     pageNumbers = []
    #     for i in results:
    #         if i.predictedPageNum != -1:
    #             pageNumbers.append(i.originalOrder)

    #     if date and len(pageNumbers) == results[0].predictedPageNumOf:
    #         file.documents.append(
    #             MLDocument(results[0].className, pageNumbers, date)
    #         )

    print("\n---\nfile id: {}".format(file.id))
    print(f"\n---\nall pages sorted: {file.allSorted}\n---")
    for i in file.documents:
        print(i.className, i.date, i.pages)

    return file
