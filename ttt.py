import numpy as np
import cv2

img_out = np.zeros((6, 8, 3))
gre = [0, 0, 0]
img_shape = img_out.shape
print(img_shape)
for length in range(img_shape[0]):
    for width in range(img_shape[1]):
        img_out[length, width, :] = gre

print(img_out)
cv2.imwrite('1.png', img_out)