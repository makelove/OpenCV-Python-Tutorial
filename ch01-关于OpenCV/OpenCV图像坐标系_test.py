# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 23:13
# @Author  : play4fun
# @File    : OpenCV图像坐标系_test.py
# @Software: PyCharm

"""
OpenCV图像坐标系_test.py:
"""

# TODO


import numpy as np
import cv2

img = cv2.imread('../data/Lenna.png', cv2.IMREAD_UNCHANGED)
print('img.shape:', img.shape)
logo = cv2.imread('../data/opencv_logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (20, 20))
print('logo.shape:', logo.shape)

cv2.imshow('src', img)
cv2.moveWindow('src', 0, 0)

# 两张图片的shape不一样
img[100:100 + logo.shape[0], 300:300 + logo.shape[1]] = logo[:, :, 0:3]
# img[10:10+logo.shape[0],30:30+logo.shape[1],:]=logo[:,:,0:3]
img[300:300 + logo.shape[1], 100:100 + logo.shape[0]] = logo[:, :, 0:3]

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text='100,300', org=(100, 300), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,
cv2.putText(img, text='300,100', org=(300, 100), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,

cv2.imshow('img+logo', img)
cv2.imwrite('img_logo.jpg',img)
cv2.moveWindow('img+logo', x=img.shape[0], y=0)
cv2.waitKey(0)
