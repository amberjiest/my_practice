import numpy as np
from MeDIT.Visualization import Imshow3DArray
import SimpleITK as sitk

def GenerateROIFromSPIN(tob_file_path, ref_image):
    '''
    This function was to read .tob file, which was designed by SPIN, MRInnovation, (by Dr. Haacke, Ying Wang.)
    :param tob_file_path: The file with '.tob'
    :param ref_image: The reference image, which provided the shape of the image
    :return: The generated ROI. Different cores was assigned to different values. The first 2 dimensions were swapped for visualization.
    
    By Jie Wu, Nov-11-18
    '''

    if isinstance(ref_image, str):
        ref_image = sitk.ReadImage(ref_image)

    image_shape = ref_image.GetSize()[0:3]
    recon_data = np.zeros(image_shape)

    index_list = np.fromfile(tob_file_path, dtype=np.uint32)

    total_roi = index_list[1]
    roi_number_index = 2
    for roi_index in range(total_roi):
        roi_point_number = index_list[roi_number_index] // 4
        print('The number of array: ', roi_point_number)
        for roi_point_index in range(1, roi_point_number):
            recon_data[index_list[roi_number_index + roi_point_index * 4 + 1],
                       index_list[roi_number_index + roi_point_index * 4 + 2],
                       index_list[roi_number_index + roi_point_index * 4 + 3]] = roi_index + 1
        roi_number_index += roi_point_number * 4 + 1

    recon_data = np.swapaxes(recon_data, 0, 1)
    return recon_data

tob_file_path = 'boundary.tob'
image_path = 'T1W.nii'
temp = GenerateROIFromSPIN(tob_file_path, image_path)
Imshow3DArray(temp)