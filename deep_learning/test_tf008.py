import numpy as np
np.random(1337)

from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

x = np.Linspace(-1, 1, 200)
np.random.shuffle(x)  # randomize the data
y = 0.5 * x + 2 + np.random.normal(0, 0.05, (200, ))
x_train, y_train = x[: 160], y[: 160]  # first 160 data points
x_test, y_test = x[160:], y[160:]  # last 40 data points
model = Sequential()
model.add(Dense(output_dim=1, input_dim=1))
model.compile(loss='mse', optimizer='sgd')
for step in range(301):
    cost = model.train_on_batch(x_train, y_train)

# save
print('test before save: ', model.predict(x_test[0:2]))
model.save('my_model.h5')  # HDF5, pip install h5py
del model  # deletes the existing model

# load
model = load_model('my_model.h5')
print('test after load: ', model.predict(x_test[0:2]))

"""
# save and load weights
model.save_weights('my_model_weights.h5
mode.load_"""