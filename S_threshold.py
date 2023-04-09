from rgb2hsv import rgb2hsv, rgb22hsv
import math
import cv2
import numpy as np
import time
from numba import jit

"""
cv2.imread -> BGR

"""
img_src = r'ziran_re.png'
img_shape = cv2.imread(img_src).shape


def rgb_read(src):
    img = cv2.imread(src)
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
    for length in range(img_shape[0]):
        starttime = time.time()
        for width in range(img_shape[1]):
            img = rgb_read(src)
            r, g, b = img[length, width, :]
            h, s, v = rgb2hsv(r, g, b)
            h_calculate = fhh(h)
            v_calculate = hvv(v)
            threshold = sth(v_calculate, h_calculate)
            if threshold > s:
                img_out[length, width, :] = gre
            else:
                img_out[length, width, :] = img[length, width, :]
        endtime = time.time()
        print('count = %d, timeUsage = %d ' % (count, endtime - starttime))
        count += 1
    img_out = img_out[:,:,::-1]
    cv2.imwrite('ziran_output.png', img_out)


s_threshold(img_src)
