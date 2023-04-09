from skimage import io, color
import numpy as np
import time
import math
import cv2
import os

# param
sig = 1/60
Lt = 80
Ct = 40
# Ci ab向量二范数 平方和开根
img_src = r'121_over3.png'
img_shape = cv2.imread('data/'+img_src).shape
name = img_src.split('.')[0]


def rgb2lab(rgb):
    # rgb = io.imread(img_src)
    lab = color.rgb2lab(rgb)
    return lab


def rgb_read(src):
    img = cv2.imread('data/'+src)
    img_rgb = img[:, :, ::-1]
    return img_rgb


def Mi(l, a, b):
    return 0.5*(math.tanh(sig*((l-Lt)+(Ct-(a**2+b**2)**0.5)))+1)


def LC(src):
    gre = [0, 255, 0]
    img_out = np.zeros(img_shape, dtype='uint8')
    count = 0
    rgb = rgb_read(src)
    lab = rgb2lab(rgb)
    for length in range(img_shape[0]):
        starttime = time.time()
        for width in range(img_shape[1]):
            l, a, b = lab[length, width, :]
            threshold = Mi(l, a, b)
            if threshold >= 0.85:
                img_out[length, width, :] = gre
            else:
                img_out[length, width, :] = rgb[length, width, :]
        endtime = time.time()
        print('count = %d, timeUsage = %d ' % (count, endtime - starttime))
        count += 1
    io.imsave(os.path.join('result', name)+'_LC085.png', img_out)


LC(img_src)

# rgb = io.imread('1_re.png')
# lab = color.rgb2lab(rgb)
# [l,a,b] = lab[0,0,:]
# print(lab)