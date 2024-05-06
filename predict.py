import numpy as np
from models.PageResult import PageResult
import tensorflow as tf

def classify(model, images, classes: list[str]):
    print("images: {}".format(len(images)))

    image_array = tf.image.resize(images, (384, 384))
    print("image shape: {}".format(image_array.shape))

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
