import SimpleITK as sitk
import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import _flatten

def AcquirePath(rootpath):
    pathlist = _flatten([[os.path.join(root, file) for file in files] for root, dirs, files in os.walk(rootpath)
                         if len(files) > 0])
    # pathlist_new = _flatten(list(filter(lambda s: len(s) > 0, pathlist)))
    return pathlist

def GetResolution(rootpath_list):
    if type(rootpath_list) is str:
        rootpath_list = [rootpath_list]
    resolution = [sitk.ReadImage(path).GetSpacing() for path in rootpath_list]
    return resolution

# def SetPathToResolution(rootpath_list):
#     resolution_dic = dict(zip(rootpath_list, GetResolution(rootpath_list)))
#     return resolution_dic

# def WrongNiiShapeFile(rootpath):
#     file_abandon = []
#     resolution_dic = SetPathToResolution(rootpath)
#     for path in resolution_dic:
#         if resolution_dic[path][0] >= 0.9 or resolution_dic[path][1] >= 0.9 or resolution_dic[path][2] >= 2:
#             file_abandon.append(path)
#     print(file_abandon)
#     return file_abandon

# def RemoveWrongShapeFile(rootpath, rootpath_list):
#     wrong_file_list = WrongNiiShapeFile(rootpath)
#     for file in rootpath_list:
#         if file in wrong_file_list:  # 如果把WrongNiiShapeFile调用放在文件中会使得每次循环时都需要调用一次函数，使得效率下降
#             os.remove(file)

def RemoveWrongNiiShapeFile(root_pathlist):
    for path in root_pathlist:
        if GetResolution(path)[0][2] >= 2.0:
            print(path)
            os.remove(path)

# def ResizeResolution(root_pathlist):
#     resolution_array_range = np.zeros((1, 2))
#     resolution_array = np.array(GetResolution(root_pathlist))
#     resolution_median = np.median(resolution_array, axis=0)
#     resolution_var = np.var(resolution_array, axis=0)
#     resolution_array_range[0] = resolution_median - 3 * resolution_var
#     resolution_array_range[1] = resolution_median + 3 * resolution_var
#     return resolution_array_range

def ExpectedResolution(root_pathlist):
    resolution_list = GetResolution(root_pathlist)
    resolution_array = np.array(resolution_list)
    resolution_median = np.median(resolution_array, axis=0)
    resolution_var = np.var(resolution_array, axis=0)
    resolution_down = resolution_median - 10 * resolution_var
    resolution_up = resolution_median + 10 * resolution_var
    print(resolution_up)
    print(resolution_down)
    count = 0
    resolution_sum = np.zeros((1, 3))
    for path in root_pathlist:
        resolution = list(_flatten(GetResolution(path)))
        if resolution_down[0] < resolution[0] < resolution_up[0] and resolution_down[1] < resolution[1] < resolution_up[1] and resolution_down[2] < resolution[2] < resolution_up[2]:
            resolution_sum += resolution
            count += 1
    resolution_range = resolution_sum / count
    print(resolution_range.flatten())
    return resolution_range.flatten()

# def AverageResolution(rootpath):
#     resolution_average = np.mean(np.array(GetResolution(rootpath)), axis=0)
#     return resolution_average

def DrawHistogram(resolution_list):
    fig, axes = plt.subplots(1, 3)
    components = ('x', 'y', 'z')
    colors = ('red', 'green', 'blue')
    for i in range(len(axes)):
        axes[i].hist(resolution_list[:, i], facecolor=colors[i])
        axes[i].set_xlabel('resolution of ' + components[i])
        axes[i].set_ylabel('value')
        axes[i].set_title('Histogram of Resolution ' + components[i])
        resolution_mean = np.mean(resolution_list[:, i])
        axes[i].vlines(resolution_mean, 0, 5, colors='k', linestyles='solid')
    plt.show()

# resolution_dic = SetPathToResolution(r'D:\abc')

# RemoveWrongShapeFile(r'D:\JSYB\GGO')

rootpath = 'D:/abc'
rootpath_f = 'D:/JSYB'
rootpath_s = r'D:\JSYB\GGO'
rootpath_t = r'D:\JSYB\ROI'

def activiate_function(rootpath):
    rootpath_list = AcquirePath(rootpath)
    resolution_list = GetResolution(rootpath_list)
    # RemoveWrongNiiShapeFile(rootpath_list)
    ExpectedResolution(rootpath_list)
    # resolution_array = np.array(resolution_list)
    # DrawHistogram(resolution_array)

# activiate_function(rootpath)
activiate_function(rootpath_f)
# activiate_function(rootpath_s)
# activiate_function(rootpath_t)

