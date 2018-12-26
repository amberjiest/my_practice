import numpy as np

image_shape = (100, 100, 20)

# Suppose you don't know the data
data = np.zeros(image_shape)
for i in range(0, image_shape[0]):
    for j in range(0, image_shape[1]):
        for k in range(0, image_shape[2]):
            if (i - 50) * (i - 50) + (j - 60) * (j - 60) + (k - 10) * (k - 10) < 64:
                data[i, j, k] = 1

x_list, y_list, z_list = np.where(data == 1)
index_list = []
for x, y, z in zip(x_list, y_list, z_list):
    index_list.append(x)
    index_list.append(y)
    index_list.append(z)
    index_list.append(0)

# print(len(index_list))
index_list.insert(0, len(index_list))
# print(len(index_list))
# print(index_list)


def GenerateData(image_shape, index_list):
    recon_data = np.zeros(image_shape)
    #
    # if len(x_list) != len(y_list) or len(z_list) != len(x_list):
    #     print('Check the length of these two lists')
    #     return

    for i in range(1, index_list[0]+1, 4):
        recon_data[index_list[i], index_list[i+1], index_list[i+2]] = 1
        # x_list.append(index_list[i])
        # y_list.append(index_list[i+1])
        # z_list.append(index_list[i+2])

    return recon_data
        # , m_list, n_list, l_list

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection="3d")


temp = GenerateData(image_shape, index_list)

print((temp == data).all())
# print(temp)
# ax.plot_surface()
# plt.show()
