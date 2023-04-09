import cv2


img_src = r'xir.png'
image = cv2.imread(img_src)


def resize(img, size):
    """

    :param img:
    :param size: tuple
    :return:
    """
    img_afre = cv2.resize(image, size)
    cv2.imwrite('xiraf.png', img_afre)


resize(image, (200, 300))
