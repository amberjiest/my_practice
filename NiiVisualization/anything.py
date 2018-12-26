import numpy as np
from MeDIT.Visualization import Imshow3DArray

image_shape = (100, 100, 20)
index_list = []
index_list.append(0)
index_list.append(2)

# Suppose you don't know the data
total_data = np.zeros(image_shape)
# roi 1
data = np.zeros(image_shape)
for i in range(0, image_shape[0]):
    for j in range(0, image_shape[1]):
        for k in range(0, image_shape[2]):
            if (i - 50) * (i - 50) + (j - 60) * (j - 60) + (k - 10) * (k - 10) < 64:
                data[i, j, k] = 1

x_list, y_list, z_list = np.where(data == 1)
index_list.append(4 * len(x_list))
for x, y, z in zip(x_list, y_list, z_list):
    index_list.append(x)
    index_list.append(y)
    index_list.append(z)
    index_list.append(0)

total_data += data
# roi 2
data = np.zeros(image_shape)
for i in range(0, image_shape[0]):
    for j in range(0, image_shape[1]):
        for k in range(0, image_shape[2]):
            if (i - 30) * (i - 30) + (j - 20) * (j - 20) + (k - 12) * (k - 12) < 49:
                data[i, j, k] = 1

x_list, y_list, z_list = np.where(data == 1)
index_list.append(4 * len(x_list))
for x, y, z in zip(x_list, y_list, z_list):
    index_list.append(x)
    index_list.append(y)
    index_list.append(z)
    index_list.append(0)

total_data += data

Imshow3DArray(total_data)
print(index_list)
