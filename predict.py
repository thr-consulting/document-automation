import numpy as np
from models.PageResult import PageResult
import tensorflow as tf

def classify(model, images, classes: list[str]):
    print("images len: {}".format(len(images)))
    width = model.input_shape[1]

    # Create a NumPy array with consistent shape
    image_array = np.zeros((len(images), width, width, 3), dtype=np.uint8)

    # Fill the array with image data
    for i, img in enumerate(images):
        image_array[i, :width, :width, :] = tf.image.resize(np.array(img), (width, width))

    scores = model.predict(image_array)
    max_index = np.argmax(scores, axis=1)

    results = []
    for i in range(len(max_index)):
        class_name = classes[max_index[i]]
        score = scores[i][max_index[i]]
        results.append(PageResult(i + 1, class_name, score))
        print("class: {}\nscore: {}".format(class_name, score))

    assert len(results)

    return results
