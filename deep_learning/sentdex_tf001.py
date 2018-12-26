import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize train_data and test_data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())  # make input be flattened or flatten these data
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # 128 units in this layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)
model.evaluate(x_test, y_test)
# return a tuple maybe i can write like this 'val_loss, val_acc = model.evaluate(x_test, y_test)'


model.save('epic_num_reader.model')

# plt.imshow(x_train[0], cmap=plt.cm.binary)
# plt.show()
# print(x_train[0])
# print(x_train[0].shape)
# print(x_train.shape)  # x_train is made up of 60,000 pictures which are all 3D matrix


