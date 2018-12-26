from MeDIT.ImageProcess import ResizeNiiFile, ResizeROINiiFile
import SimpleITK as sitk
import os
import numpy as np
from tkinter import _flatten
import shutil

def PathAcquire(path):
    pathlist = list(_flatten([[os.path.join(root, file) for file in files] for root, dirs, files in os.walk(path)
                              if len(files) > 0]))
    return pathlist

def GetResolution(root_pathlist):
    if type(root_pathlist) == str:
        root_pathlist = [root_pathlist]
    resolution = [list(sitk.ReadImage(path).GetSpacing()) for path in root_pathlist]
    return resolution

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
        if resolution_down[0] < resolution[0] < resolution_up[0] and resolution_down[2] < resolution[2] < resolution_up[2]:
            resolution_sum += resolution
            count += 1
    resolution_range = resolution_sum / count
    return resolution_range.flatten()

# def RemoveWrongNiiShapeFile(root_pathlist):
#     for path in root_pathlist:
#         if GetResolution(path)[0][2] >= 2.0:
#             os.remove(path)

def GenerateDir(rootpath, storepath):
    for root, dirs, files in os.walk(rootpath):
        for file in files:
            filename, ext = os.path.splitext(file)
            foldername, _ = os.path.splitext(filename)
            if len(files) > 0:
                rootpath_old = os.path.join(root, file)
                storepath_new = os.path.join(storepath, foldername)
                if not os.path.isdir(storepath_new):
                    os.makedirs(storepath_new)
                shutil.copy(rootpath_old, storepath_new)

# def ResizeFile(store_pathlist, resolution):
#     for store_path in store_pathlist:
#         if os.path.splitext(store_path)[1] == '.gz':
#             ResizeNiiFile(store_path, expected_resolution=resolution)
#         elif os.path.splitext(store_path)[1] == '.nii':
#             ResizeROINiiFile(store_path, expected_resolution=resolution)
#         else:
#             print('the input file should be suffix .nii or .nii.gz')
#         os.remove(store_path)

def ResizeFile(store_pathlist):
    for store_path in store_pathlist:
        if os.path.splitext(store_path)[1] == '.gz':
            ResizeNiiFile(store_path, expected_resolution=[0.6834329, 0.6834329, 1.3852941])
        elif os.path.splitext(store_path)[1] == '.nii':
            ResizeROINiiFile(store_path, expected_resolution=[0.6834329, 0.6834329, 1.3852941])
        else:
            print('the input file should be suffix .nii or .nii.gz')
        os.remove(store_path)

rootpath = 'D:/JSYB'
storepath = 'Z:/JSYB_Resize'
# rootpath = r'D:\ZJ_assignment'
# storepath = r'D:\ZJ_assignment_resize'


# root_pathlist = PathAcquire(rootpath)
# RemoveWrongNiiShapeFile(root_pathlist)

# root_pathlist_new = PathAcquire(rootpath)
# resolution = ExpectedResolution(root_pathlist_new)

GenerateDir(rootpath, storepath)

store_pathlist = PathAcquire(storepath)
ResizeFile(store_pathlist)

