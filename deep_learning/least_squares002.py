import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_raw = np.linspace(0, 100, 100)
data_size = len(x_raw)
y_raw = 0.7 * x_raw + 19 + 9.0 * np.random.rand(data_size)

x_train = x_raw/100
y_train = y_raw/100

x = tf.placeholder(tf.float64, shape=data_size)
y = tf.placeholder(tf.float64, shape=data_size)

w = tf.Variable(np.array([1.0, 10.0]))
y_pred = w[0] * x + w[1]
a = w[0]
b = w[1] * 100

loss = tf.reduce_mean(tf.squared_difference(y_pred, y))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a), sess.run(b),
          sess.run(loss, feed_dict={x: x_train, y: y_train}))
    for step in range(100):
        sess.run(train, feed_dict={x: x_train, y: y_train})
        if (step+1) % 10 == 0:
            print('{: > 3d} {: < 5f} {: < 5f} {: < 8f}'.format(step+1,
                                                               sess.run(a),
                                                               sess.run(b),
                                                               sess.run(loss, feed_dict={x: x_train, y:y_train})))
    fig, axe = plt.subplots()
    axe.scatter(x_raw, y_raw)
    y_fin = sess.run(a) * x_raw + sess.run(b)
    axe.scatter(x_raw, y_fin)
    plt.show()
