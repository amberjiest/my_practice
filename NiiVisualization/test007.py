import numpy as np
from MeDIT.Visualization import Imshow3DArray
import SimpleITK as sitk

index_list = np.load(r'D:\index_list.npy')
# image_shape = (384, 288, 64)

def image_access(image_path):
    image_read = sitk.ReadImage(image_path)
    image_content = image_read.GetSize()[0:3]
    return image_content

def GenerateData(image_shape, index_list):
    recon_data = np.zeros(image_shape)
    start = 3
    end = index_list[2] + 3
    for roi_index in range(index_list[1]):
        for index in range(start, end, 4):
            if index_list[start - 1] == 4:
                break
            if index_list[index] > image_shape[0]:
                continue
            recon_data[index_list[index], index_list[index + 1], index_list[index + 2]] = 1
        start = end + 1
        end += index_list[start-1] + 1

    return recon_data

image_path = r'D:\amberjiest\Documents\normalization_test\T1W.nii'
image_shape = image_access(image_path)
temp = GenerateData(image_shape, index_list)
Imshow3DArray(temp)