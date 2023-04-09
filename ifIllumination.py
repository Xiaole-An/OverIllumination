from rgb2hsv import rgb2hsv
import cv2
import os


def if_illumination(img):
    img_bgr = cv2.imread(img)
    b = img_bgr[:, :, 0]
    g = img_bgr[:, :, 1]
    r = img_bgr[:, :, 2]
    print(b.shape)
    length = b.shape[0]
    width = b.shape[1]
    for i in range(length):
        for j in range(width):
            b_single = b[i, j]
            g_single = g[i, j]
            r_single = r[i, j]
            h, s, v = rgb2hsv(r_single, g_single, b_single)


data_path = r'data'
for f in os.listdir(data_path):
    if_illumination(os.path.join(data_path, f))

