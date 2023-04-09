import cv2
import numpy as np
import os


def isLight(img_name, mean_gray):
    img = cv2.imread(img_name)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 获取形状以及长宽
    img_shape = gray_img.shape
    height, width = img_shape[0], img_shape[1]
    size = gray_img.size
    # 灰度图的直方图
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

    # 计算灰度图像素点偏离均值(128)程序
    a = 0
    ma = 0
    reduce_matrix = np.full((height, width), 128)
    shift_value = gray_img - reduce_matrix
    shift_sum = sum(map(sum, shift_value))

    da = shift_sum / size
    # 计算偏离128的平均偏差
    for i in range(256):
        ma += (abs(i - mean_gray - da) * hist[i])
    m = abs(ma / size)
    # 亮度系数
    k = abs(da) / m
    # print(k)
    if k[0] > 1:
        # 过亮
        if da > 0:
            print(img_name + "过亮")
        else:
            print(img_name + "过暗")
    else:
        print(img_name + "亮度正常")


def caculateGray(template):
    template = cv2.imread(template)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    h, w = template_gray.shape[:2] # template_gray 为灰度图
    m = np.reshape(template_gray, [1, w*h])
    mean = m.sum()/(w*h) # 图像平均灰度值
    return mean


test_folder = r'data'
files = os.listdir(test_folder)
gray = []
graySum = 0
for f in files:
    gray.append(caculateGray(os.path.join(test_folder, f)))
    # isLight(os.path.join(test_folder, f))


for gray_value in gray:
    graySum += gray_value

mean_gray = graySum / len(gray)
# print(mean_gray)

for f in files:
    # gray.append(caculateGray(os.path.join(test_folder, f)))
    isLight(os.path.join(test_folder, f), 10)
