import numpy as np
from MeDIT.SaveAndLoad import LoadNiiData
from MeDIT.Visualization import Imshow3DArray
#
# _, _, data = LoadNiiData(r'C:\Users\SY\Desktop\_\temp\T1W.nii')
# print(data.shape)
# Imshow3DArray(data[..., 0])
# Imshow3DArray(data[..., 1])

#
# import matplotlib.pyplot as plt
#
# with open(r'C:\Users\SY\Desktop\_\temp\boundary.tob', 'rb') as file:
#     roi_file = np.fromfile(file, dtype=np.uint32)
#     object_number = roi_file[2]
#
#     num_point = roi_file[2] // 4 - 1
#     print(roi_file[:20])
#     temp = np.reshape(roi_file[7:num_point*4+7], (-1, 4))
#     # plt.plot(temp[:, 0], 'r')
#     # plt.plot(temp[:, 1], 'g')
#     # plt.plot(temp[:, 2], 'b')
#     # plt.show()
#
#     start_point = 2
#     object_number_list = []
#     for index in range(roi_file[1]):
#         object_number = roi_file[start_point]
#         object_number_list.append(object_number)
#         print(object_number)
#
#         end_point = start_point + object_number + 1
#         start_point = end_point
#         print("")
# #
# # from MeDIT.SaveAndLoad import LoadNiiData
# # _, _, data = LoadNiiData(r'C:\Users\SY\Desktop\48\48.nii')
# # _, _, data1 = LoadNiiData(r'C:\Users\SY\Desktop\48.nii.gz', dtype=np.uint8)
# #
# # from MeDIT.Visualization import Imshow3DArray
# # from MeDIT.Normalize import NormalizeEachSlice01
# # # Imshow3DArray(data, ROI=data1)
# # Imshow3DArray(data)



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

from MeDIT.Visualization import Imshow3DArray
Imshow3DArray(total_data)
print(index_list)

def GenerateData(image_shape, index_list):
    recon_data = np.zeros(image_shape)

    for roi_index in range(index_list[1]):
        for index in range(1, index_list[0] + 1, 4):
            recon_data[index_list[index], index_list[index + 1], index_list[index + 2]] = 1

    return recon_data

import matplotlib.pyplot as plt

temp = GenerateData(image_shape, x_list, y_list)
print(temp)
plt.imshow(np.array(temp))
plt.show()


