import numpy as np
# from MeDIT.SaveAndLoad import LoadNiiData
# from MeDIT.Visualization import Imshow3DArray
#
# _, _, data = LoadNiiData(r'C:\Users\SY\Desktop\_\temp\T1W.nii')
# print(data.shape)
# Imshow3DArray(data[..., 0])
# Imshow3DArray(data[..., 1])


# import matplotlib.pyplot as plt
#
# with open(r'C:\Users\SY\Desktop\_\temp\boundary.tob', 'rb') as file:
#     roi_file = np.fromfile(file, dtype=np.uint32)
#     num_point = roi_file[2] // 4 - 1
#     print(roi_file[:20])
#     temp = np.reshape(roi_file[7:num_point*4+7], (-1, 4))
#     plt.plot(temp[:, 0], 'r')
#     plt.plot(temp[:, 1], 'g')
#     plt.plot(temp[:, 2], 'b')
#     plt.show()
#
#
# x_list, y_list, z_list = [], [], []
# roi = np.zeros((256, 256, 64))


image_shape = (100, 100)

# Suppose you don't know the data
data = np.zeros(image_shape)
data[20:30, 80:90] = 1
x_list, y_list = np.where(data == 1)




# print(x_list)
# print(y_list)

# The goal is to generate a variable named "recon_data"
# recon_data == data

def GenerateData(image_shape, x_list, y_list):
    recon_data = []
    data_color = [[0 for col in range(0, image_shape[0])] for row in range(0, image_shape[1])]

    for i in range(0, image_shape[0]):
        for j in range(0, image_shape[1]):
            if x_list[0] <= i < x_list[x_list.shape[0]-1] and y_list[0] <= j < y_list[y_list.shape[0]-1]:
                data_color[i][j] = 1
            else:
                data_color[i][j] = 0

            recon_data.append(data_color[i][j])

    return np.array(recon_data).reshape(100,100)
    # return recon_data


import matplotlib.pyplot as plt

temp = GenerateData(image_shape, x_list, y_list)
print(temp)
plt.imshow(temp, cmap='gray')
plt.show()