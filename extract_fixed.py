import cv2
from layouts import Coordinate, Layout, PageCoordinate


start_point = None
end_point = None
image = None
drawing = False
original_image = None


class ExtractCoordinates:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def get_mouse_coordinates(event, x, y, flags, param):
    global start_point
    global drawing
    global end_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            image[:] = original_image[:]
            cv2.rectangle(image, start_point, (x, y), (0, 0, 255), 2)
            cv2.imshow("Image", image)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(image, start_point, (x, y), (0, 0, 255), 2)
        cv2.imshow("Image", image)
        h, w, channel = image.shape
        print(
            '\n"x": {},\n"y": {},\n"width": {},\n"height": {}'.format(
                start_point[0] / w,
                start_point[1] / h,
                (end_point[0] - start_point[0]) / w,
                (end_point[1] - start_point[1]) / h,
            )
        )
        print(
            "\n{}, {}, {}, {}".format(
                start_point[0] / w,
                start_point[1] / h,
                (end_point[0] - start_point[0]) / w,
                (end_point[1] - start_point[1]) / h,
            )
        )


def get_coordinates_from_image(image_path):
    # Load the image
    global image
    global original_image

    image = cv2.imread(image_path)
    original_image = image.copy()

    print("Image width and height: {} - {}".format(image.shape[0], image.shape[1]))

    # Display the image with the bounding box
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1024, 960)
    cv2.setMouseCallback("Image", get_mouse_coordinates)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "/home/roland/dataset_2024/jpg_original/Scotia Credit/scotiaCC96-2.jpg"

get_coordinates_from_image(image_path)

# layout = Layout(
#     "RBC Bank",
#     [
#         PageCoordinate(
#             1,
#             dd_of_dd,
#             0.9003921568627451,
#             0.8703030303030304,
#             0.08941176470588236,
#             0.0503030303030303,
#         )
#     ],
#     [
#         Coordinate(
#             1,
#             0.596078431372549,
#             0.13333333333333333,
#             0.396078431372549,
#             0.044848484848484846,
#         )
#     ],
# )


# text = extract_text(image_path, layout.pageNumber[0])
# processPageRegex(dd_of_dd, text)
# extract_text(image_path, layout.date[0])
