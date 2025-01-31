import cv2


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
image_path = "/media/roland/dataset_backup/dataset/dataset_2024/jpg_original/Valley Fiber/heocr9085-1.jpg"

get_coordinates_from_image(image_path)
