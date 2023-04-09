from PIL import Image
import os
from os import listdir
from tools import calLaplacianVar,overExposeDetect


def check_image(img_path, fixedSize, stdTimes = 1):
    #正常值区间
    # distArea = []
    # distArea.append(calAvg(img) - calStd(img)*stdTimes)
    # distArea.append(calAvg(img) + calStd(img)*stdTimes)
    status = "normal"
    #当图片指标不在正常范围内,被判断为异常
    value = calLaplacianVar(img_path, fixedSize)
    if (value < 2200):
        isOutlier = True
        status = "vague"
        print(str(img_path) + "该图指标值:" + str(value) + " status:" + status)
        print(" 正常区间:[2200 , +)")
        return isOutlier
    else:
        isOutlier = False
    # print("该图指标值:" + str(value) + " status:" + status)
    isOutlier = overExposeDetect(img_path, fixedSize)
    return isOutlier


def main():
    test_folder = r'data'
    #generate_folder = r'E:\newproject\generate'
    files = listdir(test_folder)
    for f in files:
        # print("图片" + f +":")
        check_image(os.path.join(test_folder, f), (448, 448))


if __name__ == '__main__':
    main()
