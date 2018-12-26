import numpy as np
import matplotlib.pyplot as plt
# x = range(1, 101, 2)
x = np.linspace(0, 1, 100)
a = np.linspace(0, 1, 100)
# e = np.ones((100, 1))
y = x.T * np.log(a)
z = (1 - x).T * np.log(1 - a)
plt.plot(x, y, label='1')
plt.plot(x, z, label='2')
plt.show()


