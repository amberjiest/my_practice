import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

image_shape = (100, 100, 20)

# Suppose you don't know the data
data = np.zeros(image_shape)
for i in range(0, image_shape[0]):
    for j in range(0, image_shape[1]):
        for k in range(0, image_shape[2]):
            if (i - 50) * (i - 50) + (j - 60) * (j - 60) + (k - 10) * (k - 10) < 64:
                data[i, j, k] = 1

x_list, y_list, z_list = np.where(data == 1)

fig = plt.figure()
ax = fig.gca(projection="3d")

ax.plot_surface(x_list, y_list, z_list)
plt.show()