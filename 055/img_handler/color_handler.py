# coding:utf8
import cv2
from PIL import Image


def color_setter(color='REAL'):
    if color == 'GRAY':
        img = cv2.imread('./temp/img/tmp.png', 0)
        cv2.imwrite('./temp/out/tmp_out.png', img)
    if color == 'REAL':
        img = cv2.imread('./temp/img/tmp.png')
        cv2.imwrite('./temp/out/tmp_out.png', img)
    # if color == 'OLD':
    #     img = cv2.imread('./temp/img/tmp.png')
    if color == 'BW':
        img = Image.open('./temp/img/tmp.png')
        Img = img.convert('L')
        # Img.save("./temp/out/tmp_out.png")
        threshold = 200
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        photo = Img.point(table, '1')
        photo.save("./temp/out/tmp_out.png")


    return
