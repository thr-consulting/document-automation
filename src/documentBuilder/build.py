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

    print("\n---\nfile id: {}".format(file.id))
    print(f"\n---\nall pages sorted: {file.allSorted}\n---")
    for i in file.documents:
        print(i.className, i.date, i.pages)

    return file
