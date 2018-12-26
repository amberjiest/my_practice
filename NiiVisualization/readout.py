import os
import numpy as np
from nibabel.testing import data_path
import nibabel as nib

# nib.Nifti1Header.quaternion_threshold = - np.finfo(np.float32).eps * 10
# img = nib.load(r'D:\amberjiest\Documents\normalization_test\T1W.nii')
# img_arr = img.get_fdata()
# print(img_arr)
# # img_arr = np.squeeze(img_arr)
# io.imshow(img_arr)

image_content = os.path.join(r'D:\amberjiest\Documents\normalization_test', 'T1W.nii')
img = nib.load(image_content)
print(img.shape)
