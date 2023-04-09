import numpy as np
import cv2


def yuan_LBP(img, r=3, p=8):
    h, w = img.shape
    dst = np.zeros((h, w), dtype=img.dtype)
    for i in range(r, h - r):
        for j in range(r, w - r):
            LBP_str = []
            for k in range(p):
                rx = i + r * np.cos(2 * np.pi * k / p)
                ry = j - r * np.sin(2 * np.pi * k / p)
                # print(rx, ry)
                x0 = int(np.floor(rx))
                x1 = int(np.ceil(rx))
                y0 = int(np.floor(ry))
                y1 = int(np.ceil(ry))

                f00 = img[x0, y0]
                f01 = img[x0, y1]
                f10 = img[x1, y0]
                f11 = img[x1, y1]
                w1 = x1 - rx
                w2 = rx - x0
                w3 = y1 - ry
                w4 = ry - y0
                fxy = w3 * (w1 * f00 + w2 * f10) + w4 * (w1 * f01 + w2 * f11)
                if fxy >= img[i, j]:
                    LBP_str.append(1)
                else:
                    LBP_str.append(0)
            LBP_str = ''.join('%s' % id for id in LBP_str)
            dst[i, j] = int(LBP_str, 2)
    return dst


def main():
    img_src = r'data/121_over1.png'
    img = cv2.imread(img_src, 0)
    print(img.shape)
    cv2.imwrite('data/121_over1_done.png', yuan_LBP(img), )


if __name__ == '__main__':
    main()
