import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

# RMSprop 在加速神经网络训练中有提到

# download the mnist to the path '~/.keras/datasets/' if it is first time to be called
# X shape(60,000 28x28), y shape(10,000,)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data pre-processing
X_train = X_train.reshape(X_train.shape[0], -1) / 255  # normalize
X_test = X_test.reshape(X_test.shape[0], -1) / 255  # normalize
y_train = np_utils.to_categorical(y_train, num_classes=10)  # np_utils.to_categorical将输出值转化为 one-hot code
y_test = np_utils.to_categorical(y_test, num_classes=10)

# Another way to build your neuralnet
    # model = Sequential()
    # model.add(...)
model = Sequential([
    Dense(32, input_dim=784),  # 从原来784像素的图中提取32个feature
    Activation('relu'),  # 将32个feature放进激活层，将这些数据变为非线性化的
    Dense(10),  # 2层神经网络输出为10个单位
    Activation('softmax')
])
# Another way to define your optimizer
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# We add metrics to get more results you want to see
model.compile(
    optimizer=rmsprop,  # 如果用optimizer='rmsprop'就是使用默认的rmsprop
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

print('Training --------')
#Anthor way to train the method
model.fit(X_train, y_train, nb_epoch=2, batch_size=32)

print('\n Testing --------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(X_test, y_test)

print('test loss', loss)
print('test accuracy', accuracy)


