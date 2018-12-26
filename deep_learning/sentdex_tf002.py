import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict([x_test])

print(predictions)

import numpy as np

# print(np.argmax(predictions[0]))
print(predictions[0])

plt.imshow(x_test[0])
plt.show()

