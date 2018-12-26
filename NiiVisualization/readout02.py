import SimpleITK as sitk

image_path = r'D:\amberjiest\Documents\normalization_test\T1W.nii'
image_read = sitk.ReadImage(image_path)
image_content = sitk.GetArrayViewFromImage(image_read)
image_shape = image_read.GetSize()[0:3]
print(image_content.shape)
print(type(image_read))
print(image_read.GetSize())
print(image_shape)
