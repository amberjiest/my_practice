import matplotlib.pyplot as plt
import math
import numpy as np


plt.figure(1)

x = []
y = []
# z = []

a = np.linspace(-10, 10, 1000)

for i in a:
    x.append(i)
    y.append(math.cos(i) * math.exp(-i))
    # y.append(math.sin(i) / i)

plt.plot(x, y)

plt.show()