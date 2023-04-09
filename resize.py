import cv2


img_src = r'data/ziran1.png'
image = cv2.imread(img_src)


def resize(img, size):
    """

    :param img:
    :param size: tuple
    :return:
    """
    img_afre = cv2.resize(image, size)
    cv2.imwrite('ziran_re.png', img_afre)


resize(image, (200, 200))
