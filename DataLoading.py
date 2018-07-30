# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:41:08 2018

@author: 212710461
"""

import pandas as pd
import os, time
from radiomics import featureextractor
import SimpleITK as sitk

# =============================================================================
# #------------------------Read Dicom file---------------------------
# filename = get_testdata_files("C:/Users/212710461/Desktop/Lung data/PHDP test data/PeviT/data/73629041jiangxinruiT1C/73629041_20140107_MR_6_18_01.dcm")
# ds1 = pydicom.dcmread("C:/Users/212710461/Desktop/Lung data/PHDP test data/PeviT/data/73629041jiangxinruiT1C/73629041_20140107_MR_6_18_01.dcm")
# ds2 = pydicom.dcmread("C:/Users/212710461/Desktop/Lung data/PHDP test data/LungCancer/LUNG1-001/ct.0.dcm")
# #print(ds1) 
# #plt.imshow(ds1.pixel_array)
# #plt.imshow(ds2.pixel_array)
# # ds.pixel_array is in numpy.array type.
# #print(type(ds1.pixel_array))
# #------------------------------------------------------------------
# 
# # -----------------------Read NifTi file---------------------------
# data1 = nib.load("C:/Users/212710461/Desktop/Lung data/PHDP test data/PeviT/ROI/73629041jiangxinruiT1C_merge.nii")
# img = data1.get_data()
# #------------------------------------------------------------------
# 
# =============================================================================

#----------------------------Using SITK to import image and mask-----------------------




#imagepath_1, labelpath_1 = getTestCase("C:/Users/212710461/Desktop/Lung data/PHDP test data/PeviT/data/73629041jiangxinruiT1C/73629041_20140107_MR_6_18_01.dcm")


# ----------------------------Reading dicom in single ---------------------------


def readSingle(path):
    files = os.listdir(path)
    dicom_dir = []
    for file in files:
        full_dir = path + '/' + file
        dicom_dir.append(full_dir)
    # Read in the image
    images = []
    for file_path in dicom_dir:
        dicom = sitk.ReadImage(file_path)
        images.append(dicom)
    return images
# ----------------------------------------------------------------------


# ----------------------------Reading dicom in series ---------------------------

#path = "C:/Users/212710461/Desktop/Lung data/PHDP test data/PeviT/data" # 图像文件夹目录

def readAll(path):
    folders = os.listdir(path)
    dicom_dir = []
    for folder in folders:
        sub_dir = []
        sub_path = path + '/' + folder
        files = os.listdir(sub_path)
        for file in files:
            sub_sub_path = sub_path + '/' + file
            sub_dir.append(sub_sub_path)
        dicom_dir.append(sub_dir)

    # Read in the image
    images = []
    for file_path in dicom_dir:
        dicom = sitk.ReadImage(file_path)
        #print(file_path, ' has been read in.')
        images.append(dicom)
    return images
# ----------------------------------------------------------------------

# ------------------------------Reading nifti---------------------------
def readROI(path):
    files = os.listdir(path)
    nifti_dir = []
    for file in files:
        sub_path = path + '/' + file
        nifti_dir.append(sub_path)

    # Read in the ROI
    labels = []
    for file_path in nifti_dir:
        nifti = sitk.ReadImage(file_path)
        #print(file_path, ' has been read in.')
        labels.append(nifti)
    return labels
# ----------------------------------------------------------------------


# =============================================================================
# # --------------------Plot the image-------------------------------
# plt.figure(figsize = (20, 20))
# # First image
# plt.subplot(2, 1, 1)
# plt.imshow(sitk.GetArrayFromImage(image_1)[0,:,:], cmap="gray")
# plt.title("Brain #1")
# plt.subplot(2, 1, 2)
# plt.imshow(sitk.GetArrayFromImage(label_1)[3,:,:])        
# plt.title("Segmentation #1")
# #---------------------------------------------------------------------------------------
# =============================================================================


# ----------------------Extract the features ----------------------------------
def extract(images, labels):
    column_name = ['general_info_VolumeNum',
                   'general_info_VoxelNum',
                   'original_shape_Elongation',
                   'original_shape_Flatness',
                   'original_shape_LeastAxis',
                   'original_shape_MajorAxis',
                   'original_shape_Maximum2DDiameterColumn',
                   'original_shape_Maximum2DDiameterRow',
                   'original_shape_Maximum2DDiameterSlice',
                   'original_shape_Maximum3DDiameter',
                   'original_shape_MinorAxis',
                   'original_shape_Sphericity',
                   'original_shape_SurfaceArea',
                   'original_shape_SurfaceVolumeRatio',
                   'original_shape_Volume',
                   'original_firstorder_10Percentile',
                   'original_firstorder_90Percentile',
                   'original_firstorder_Energy',
                   'original_firstorder_Entropy',
                   'original_firstorder_InterquartileRange',
                   'original_firstorder_Kurtosis',
                   'original_firstorder_Maximum',
                   'original_firstorder_MeanAbsoluteDeviation',
                   'original_firstorder_Mean',
                   'original_firstorder_Median',
                   'original_firstorder_Minimum',
                   'original_firstorder_Range',
                   'original_firstorder_RobustMeanAbsoluteDeviation',
                   'original_firstorder_RootMeanSquared',
                   'original_firstorder_Skewness',
                   'original_firstorder_TotalEnergy',
                   'original_firstorder_Uniformity',
                   'original_firstorder_Variance',
                   'original_glcm_Autocorrelation',
                   'original_glcm_ClusterProminence',
                   'original_glcm_ClusterShade',
                   'original_glcm_ClusterTendency',
                   'original_glcm_Contrast',
                   'original_glcm_Correlation',
                   'original_glcm_DifferenceAverage',
                   'original_glcm_DifferenceEntropy',
                   'original_glcm_DifferenceVariance',
                   'original_glcm_Id',
                   'original_glcm_Idm',
                   'original_glcm_Idmn',
                   'original_glcm_Idn',
                   'original_glcm_Imc1',
                   'original_glcm_Imc2',
                   'original_glcm_InverseVariance',
                   'original_glcm_JointAverage',
                   'original_glcm_JointEnergy',
                   'original_glcm_JointEntropy',
                   'original_glcm_MaximumProbability',
                   'original_glcm_SumAverage',
                   'original_glcm_SumEntropy',
                   'original_glcm_SumSquares',
                   'original_gldm_DependenceEntropy',
                   'original_gldm_DependenceNonUniformity',
                   'original_gldm_DependenceNonUniformityNormalized',
                   'original_gldm_DependenceVariance',
                   'original_gldm_GrayLevelNonUniformity',
                   'original_gldm_GrayLevelVariance',
                   'original_gldm_HighGrayLevelEmphasis',
                   'original_gldm_LargeDependenceEmphasis',
                   'original_gldm_LargeDependenceHighGrayLevelEmphasis',
                   'original_gldm_LargeDependenceLowGrayLevelEmphasis',
                   'original_gldm_LowGrayLevelEmphasis',
                   'original_gldm_SmallDependenceEmphasis',
                   'original_gldm_SmallDependenceHighGrayLevelEmphasis',
                   'original_gldm_SmallDependenceLowGrayLevelEmphasis',
                   'original_glrlm_GrayLevelNonUniformity',
                   'original_glrlm_GrayLevelNonUniformityNormalized',
                   'original_glrlm_GrayLevelVariance',
                   'original_glrlm_HighGrayLevelRunEmphasis',
                   'original_glrlm_LongRunEmphasis',
                   'original_glrlm_LongRunHighGrayLevelEmphasis',
                   'original_glrlm_LongRunLowGrayLevelEmphasis',
                   'original_glrlm_LowGrayLevelRunEmphasis',
                   'original_glrlm_RunEntropy',
                   'original_glrlm_RunLengthNonUniformity',
                   'original_glrlm_RunLengthNonUniformityNormalized',
                   'original_glrlm_RunPercentage',
                   'original_glrlm_RunVariance',
                   'original_glrlm_ShortRunEmphasis',
                   'original_glrlm_ShortRunHighGrayLevelEmphasis',
                   'original_glrlm_ShortRunLowGrayLevelEmphasis',
                   'original_glszm_GrayLevelNonUniformity',
                   'original_glszm_GrayLevelNonUniformityNormalized',
                   'original_glszm_GrayLevelVariance',
                   'original_glszm_HighGrayLevelZoneEmphasis',
                   'original_glszm_LargeAreaEmphasis',
                   'original_glszm_LargeAreaHighGrayLevelEmphasis',
                   'original_glszm_LargeAreaLowGrayLevelEmphasis',
                   'original_glszm_LowGrayLevelZoneEmphasis',
                   'original_glszm_SizeZoneNonUniformity',
                   'original_glszm_SizeZoneNonUniformityNormalized',
                   'original_glszm_SmallAreaEmphasis',
                   'original_glszm_SmallAreaHighGrayLevelEmphasis',
                   'original_glszm_SmallAreaLowGrayLevelEmphasis',
                   'original_glszm_ZoneEntropy',
                   'original_glszm_ZonePercentage',
                   'original_glszm_ZoneVariance',
                   'original_ngtdm_Busyness',
                   'original_ngtdm_Coarseness',
                   'original_ngtdm_Complexity',
                   'original_ngtdm_Contrast',
                   'original_ngtdm_Strength']

    del_name = ['general_info_BoundingBox',
                'general_info_EnabledImageTypes',
                'general_info_GeneralSettings',
                'general_info_ImageHash',
                'general_info_ImageSpacing',
                'general_info_MaskHash',
                'general_info_NumpyVersion',
                'general_info_PyWaveletVersion',
                'general_info_SimpleITKVersion',
                'general_info_Version']


    # Initialize the dataframe to store the calculation results
    df = pd.DataFrame(columns = column_name)

    extractor = featureextractor.RadiomicsFeaturesExtractor()

    df_list = [df]
    for (image, label) in zip(images, labels):
        result = extractor.execute(image, label)
        for name in del_name:
            del result[name]
        sub_df = pd.DataFrame(result, index = [0])
        df_list.append(sub_df)

    df = pd.concat(df_list, ignore_index = True)
    return df
# -----------------------------------------------------------------

#---------------------save as csv----------------------------------
def write(df):
    localtime = time.asctime(time.localtime(time.time()))
    localtime = localtime.replace(" ", "_")
    localtime = localtime.replace(":", "_")
    save_name = "Features_Exraction_Result_" + localtime + ".csv"
    #print(save_name)
    df.to_csv(save_name)
# ---------------------------------------------------------------



