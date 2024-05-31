import numpy as np
from models.PageResult import PageResult
import tensorflow as tf

def classify(model, images, classes: list[str]):
    print("images len: {}".format(len(images)))

    # Create a NumPy array with consistent shape
    image_array = np.zeros((len(images), 384, 384, 3), dtype=np.uint8)

    # Fill the array with image data
    for i, img in enumerate(images):
        image_array[i, :384, :384, :] = tf.image.resize(np.array(img), (384, 384))
    
    
    # image_array = tf.image.resize(images, (384, 384))
    # print("image shape: {}".format(image_array.shape))

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
