# coding:utf8
import cv2
import numpy as np


def change_youhua1(ero=2, dil=3):

    img = cv2.imread('./temp/out/tmp_out.png')
    kernel = np.ones((4, 4), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=ero)
    dilation = cv2.dilate(erosion, kernel, iterations=5)
    cv2.imwrite('./temp/out/tmp_out.png', dilation)

    return



