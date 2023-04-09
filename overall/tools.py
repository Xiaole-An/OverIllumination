import cv2
import os
import numpy as np
import math

'''
@illustrate：用拉普拉斯计算图片模糊程度
@param img 图片路径， size(tuple)resize大小
@return 模糊程度
'''
def calLaplacianVar(img, size):
    grayImg = cv2.imread(img, 0)
    grayImg = cv2.resize(grayImg, size)
    sobelImg = cv2.Laplacian(grayImg, cv2.CV_64FC1)
    #标准差
    mu, sigma = cv2.meanStdDev(sobelImg)
    sigmaValue = sigma[0][0]
    #方差
    variance = pow(sigmaValue, 2)
    return variance


"""
@illustrate: 曝光检测
@param
"""
def overExposeDetect(img_path,size):
    img = cv2.imread(img_path, 1)
    img = cv2.resize(img, size)
    thre = 0.175
    status = "normal"
    flag = False
    if img.shape[2] != 1:
        hsvSpaceImage = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) # hsv转换
    else:
        hsvSpaceImage = img.clone()
    hsvImageVChannels = hsvSpaceImage[:, :, 2]
    step = 8   #以8*8小窗口遍历V通道图像
    imageOverExposeBlockNum = 0
    imageBlocks = 0
    imageDarkBlockNum = 0
    #遍历
    i = 0
    while i < hsvImageVChannels.shape[0]:
        j = 0
        while j < hsvImageVChannels.shape[1]:
            imageBlock = hsvImageVChannels[i:i+step, j:j+step]
            mea = np.mean(imageBlock)# 求小矩形的均值
            if mea > 233.0:
                imageOverExposeBlockNum += 1
            elif mea < 53.0:
                imageDarkBlockNum += 1
            imageBlocks += 1
            j += step
        i += step
    if imageDarkBlockNum/imageBlocks > thre:
        status = "dark"
        flag = True
    if imageOverExposeBlockNum/imageBlocks > thre:
        status = "overexposure"
        flag = True
    if flag == True:
        print(str(img_path) + "该图曝光度:" + str(imageOverExposeBlockNum/imageBlocks * 100) + " status:" + status)
        print(" 正常区间:(0," + str(thre*100) + "]")
    return flag
