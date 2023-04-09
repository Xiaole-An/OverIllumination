import os.path

from rgb2hsv import rgb2hsv
import math
import cv2
import numpy as np
import time
from numba import jit
from skimage import io, color

"""
cv2.imread -> BGR

"""
img_src = r'121_over1.png'
img_shape = cv2.imread('data/'+img_src).shape
name = img_src.split('.')[0]
# a = os.path.join('result', name)+'_S.png'
# print(a)


def rgb_read(src):
    img = cv2.imread('data/'+src)
    img_rgb = img[:, :, ::-1]
    return img_rgb


def fhh(h):
    return 17 * math.exp(-((h-30)/11.46) ** 2) + 30015 * math.exp(-((h-136.3)/100.1) ** 2) - 29999 * math.exp(-((h-136.3)/100) ** 2)


def hvv(v):
    return math.exp(2.4 * (v-255) / 255)


def sth(v, h):
    return hvv(v) * fhh(h)


# print(rgb_read(img_src))

def s_threshold(src):
    """

    :param src:
    :return:
    :gre: 填充颜色中间变量 0 255 0为绿色
    """
    gre = [0, 255, 0]
    img_out = np.zeros(img_shape, dtype='uint8')
    count = 0
    img = rgb_read(src)
    hsv = color.rgb2hsv(img)
    for length in range(img_shape[0]):
        starttime = time.time()
        for width in range(img_shape[1]):
            h, s, v = hsv[length, width, :]
            h = h*180
            s = s*255
            v = v*255
            h_calculate = fhh(h)
            v_calculate = hvv(v)
            threshold = sth(v_calculate, h_calculate)
            if threshold > s+3.2:
                img_out[length, width, :] = gre
            else:
                img_out[length, width, :] = img[length, width, :]
        endtime = time.time()
        print('count = %d, timeUsage = %d ' % (count, endtime - starttime))
        count += 1
    img_out = img_out[:, :, ::-1]
    cv2.imwrite(os.path.join('result', name)+'_S+3-2.png', img_out)


s_threshold(img_src)
