import numpy as np
import matplotlib.pyplot as plt

image_shape = (100, 100)

# Suppose you don't know the data
data = np.zeros(image_shape)
for i in range(0, image_shape[0]):
    for j in range(0, image_shape[1]):
        if (i - 50) * (i - 50) + (j - 60) * (j - 60) < 100:
            data[i, j] = 1
x_list, y_list = np.where(data == 1)

# The goal is to generate a variable named "recon_data"
# recon_data == data
def GenerateData(image_shape, x_list, y_list):
    recon_data = []
    recon_color = np.zeros(image_shape)

    for row in range(0, len(x_list)):
        recon_color[x_list[row]][y_list[row]] = 1
    return recon_color
    # return recon_data

temp = GenerateData(image_shape, x_list, y_list)
print(temp)
plt.imshow(temp, cmap='gray')
plt.show()
