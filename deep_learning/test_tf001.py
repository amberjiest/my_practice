# 回归问题 regressor
import numpy as np
np.random.seed(1337)  # reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

#  create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)  # randomize the data
y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200,))

# plot data
plt.scatter(X, y)
plt.show()

X_train, y_train = X[:160], y[:160]  # first 160 data points
X_test, y_test = X[160:], y[160:]  # last 40 data points

# build a neural network from the 1st layer to the last layer
model = Sequential()
# 因为我们这里解决的是一个输入对应一个输出的线性方程，所以每个样本的输入与输出都是一个
model.add(Dense(output_dim=1, input_dim=1))
# 往后定义第二层的时候，第二层的输入就是上一层的输出
# model.add(Dense(output_dim=1))

# choose loss function and optimizing method
model.compile(loss='mse', optimizer='sgd')

# training
print("Training ---------")
for step in range(301):
    cost = model.train_on_batch(X_train, y_train)
    # 本函数在一个batch的数据上进行一次参数更新，函数返回训练误差的标量值或标量值的list，与evaluate的情形相同。
    if step % 100 == 0:
        print('train cost', cost)

# test
print('\n Tesing -------')
cost = model.evaluate(X_test, y_test, batch_size=40)
print('test cost', cost)
w, b = model.layers[0].get_weights()
print('Weights=', w, 'bias', b )

# plotting the prediction
y_pred = model.predict(X_test)
plt.scatter(X_test, y_pred)
plt.plot(X_test, y_pred)
plt.show()