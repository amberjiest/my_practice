from MeDIT.ImageProcess import ResizeNiiFile, ResizeROINiiFile
import SimpleITK as sitk
import os
import numpy as np
from tkinter import _flatten
import shutil

def PathAcquire(rootpath):
    pathlist = list(_flatten([[os.path.join(root, file) for file in files] for root, dirs, files in os.walk(rootpath)
                              if len(files) > 0]))
    # pathlist_new = list(_flatten(list(filter(lambda s: len(s) > 0, pathlist))))
    return pathlist

def GetResolution(rootpath):
    resolution = [list(sitk.ReadImage(nii_file).GetSpacing()) for nii_file in PathAcquire(rootpath)]
    return resolution

def SetPathToResolution(rootpath):
    resolution_dic = dict(zip(PathAcquire(rootpath), GetResolution(rootpath)))
    return resolution_dic

def AverageResolution(rootpath):
    resolution_average = np.mean(np.array(GetResolution(rootpath)), axis=0)
    return resolution_average

def WrongNiiShapeFile(rootpath):
    file_abandon = []
    resolution_dic = SetPathToResolution(rootpath)
    for path in resolution_dic:
        if resolution_dic[path][0] >= 0.9 or resolution_dic[path][1] >= 0.9 or resolution_dic[path][2] >= 2:
            file_abandon.append(path)
    return file_abandon

def RemoveWrongShapeFile(rootpath):
    file_list = PathAcquire(rootpath)
    print(file_list)
    for file in file_list:
        if file in WrongNiiShapeFile(rootpath):
            os.remove(file)

def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

def GeneratePath(rootpath, storepath):
    shutil.copytree(rootpath, storepath)

def GenerateFileName(rootpath, storepath, name):
    storepath_new = []
    if os.path.splitext(rootpath)[1] == '.nii':
        storepath_new = storepath + '/' + rootpath[7:-4] + '_' + name + '.nii'
    elif os.path.splitext(rootpath)[1] == '.gz':
        storepath_new = storepath + '/' + rootpath[7:-7] + '_' + name + '.nii.gz'
    else:
        print('the input file should be suffix .nii or .nii.gz')
    return storepath_new

def ResizeNii(rootpath, storepath):
    ResizeNiiFile(rootpath, storepath, expected_resolution=AverageResolution(rootpath))

def ResizeNiiROI(rootpath, storepath):
    ResizeROINiiFile(rootpath, storepath, expected_resolution=AverageResolution(rootpath))

def Show_resolution(rootpath):
    resolution_list = [sitk.ReadImage(path).GetSpacing() for path in PathAcquire(rootpath)]
    print(resolution_list)

def Show_shape(rootpath):
    shape_list = np.array([sitk.GetArrayFromImage(sitk.ReadImage(path)) for path in PathAcquire((rootpath))])
    print(shape_list.shape)

RemoveWrongShapeFile('D:/abc')
shutil.copytree(r'D:\abc', 'D:/abc_resized', ignore=ig_f)
ResizeNii(r'D:\abc', 'D:/abc_resized')
# RemoveWrongShapeFile('')
# ResizeNiiROI(r'')
Show_resolution(r'D:\abc')
Show_resolution(r'D:\abc_resize')
# Show_shape(r'D:\abc')


