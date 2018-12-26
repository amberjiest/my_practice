import SimpleITK as sitk
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

def GetSpecificPath(path):
    sub_path = os.path.join(path, '*.nii*')
    path_list = glob.glob(sub_path)
    return path_list

def GetResolution(rawpath):
    nii_files = GetSpecificPath(rawpath)
    resolution = [list(sitk.ReadImage(nii_file).GetSpacing()) for nii_file in nii_files]
    # resolution = []
    # for nii_file in nii_files:
    #     nii_image = sitk.ReadImage(nii_file)
    #     resolution.append(list(nii_image.GetSpacing()))
        # print(resolution)
        # print(type(resolution[0]))
    return resolution

# def AcquirePath(rootpath):
#     if os.listdir(rootpath) is not None:
#         path_update = []
#         for file in os.listdir(rootpath):
#             path_update = os.path.join(rootpath, file)
#         for i in range(len(path_update)):
#             AcquirePath(path_update[i])
#     else:
#         pass

def DrawHistogram(resolution_list):
    fig, axes = plt.subplots(1, 3)
    components = ('x', 'y', 'z')
    colors = ('red', 'green', 'blue')
    for i in range(len(resolution_list)):
        axes[i].hist(resolution_list[:, i], facecolor=colors[i])
        axes[i].set_xlabel('resolution of ' + components[i])
        axes[i].set_ylabel('value')
        axes[i].set_title('Histogram of Resolution ' + components[i])
    plt.show()



    # ax1 = plt.subplot(131)
    # ax1.hist(resolution_list[:, 0], facecolor='red')
    # plt.xlabel('resolution of x')
    # plt.ylabel('value')
    # plt.title('Histogram of Resolution x')
    # plt.grid(True)
    #
    # ax1 = plt.subplot(132)
    # ax1.hist(resolution_list[:, 1], facecolor='green')
    # plt.xlabel('resolution of y')
    # plt.ylabel('value')
    # plt.title('Histogram of Resolution y')
    # plt.grid(True)
    #
    # ax1 = plt.subplot(133)
    # ax1.hist(resolution_list[:, 2], facecolor='blue')
    # plt.xlabel('resolution of z')
    # plt.ylabel('value')
    # plt.title('Histogram of Resolution z')
    # plt.grid(True)
    #
    # plt.show()


# a = GetResolution(r'Z:\abc')
# resolution_list = np.array(a)
# resolution_list = np.array(GetResolution(r'Z:\abc'))
# print(resolution_list.shape)
# DrawHistogram(resolution_list)

resolution_list = np.array(GetResolution(r'Z:\JSYB\GGO\AIS_nii'))
DrawHistogram(resolution_list)

# resolution_list = np.array(GetResolution(r'Z:\JSYB\GGO\AIS_nii'))
# DrawHistogram(resolution_list)



# sub_path = []
# for root, dirs, files in os.walk(rawpath):
#     for dir in files:
#         sub_path = os.path.join(rawpath, dir)
#     # path_list = glob.glob(sub_path)

# GetResolution(r'Z:\JSYB\GGO\AIS_nii\598742.nii.gz')

# print(np.array(resolution_list).shape)
# resolution_list.ravel()

# colors = ('red', 'blue', 'lightgreen')
# coordinate = ('x', 'y', 'z')
# for i in range(3):
#     plt.hist(resolution_list[:, i], facecolor=colors[i])
#     plt.xlabel('resolution of ' + coordinate[i])
#     plt.ylabel('value')
#     plt.title('Histogram of Resolution of' + coordinate[i])
#     plt.grid(Ture)
#     plt.show()


# print(resolution_list[:, 1])

# import os
# for sub_case in os.listdir(r'Z:\abc'):
#     print(sub_case)
