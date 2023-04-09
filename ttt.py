import numpy as np
import cv2
import math
from skimage import io, color
sig = 1/60
Lt = 80
Ct = 40
# img_out = np.zeros((6, 8, 3))
# gre = [0, 0, 0]
# img_shape = img_out.shape
# print(img_shape)
# for length in range(img_shape[0]):
#     for width in range(img_shape[1]):
#         img_out[length, width, :] = gre
#
# print(img_out)
# cv2.imwrite('1.png', img_out)
rgb = io.imread('1_re.png')
lab = color.rgb2lab(rgb)
hsv = color.rgb2hsv(rgb)
h,s,v = hsv[0,0,:]

LC = 0.5*(math.tanh(sig*((l-Lt)+(Ct-(a**2+b**2)**0.5)))+1)
print(LC)

img = cv2.imread('data/121_over1.png').shape
imgs = io.imread('data/121_over1.png').shape
print(img, imgs)