# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 11:05
# @Author  : play4fun
# @File    : HoughCircles_chess.py
# @Software: PyCharm

"""
HoughCircles_chess.py:
围棋
"""

import cv2
import numpy as np
from collections import Counter


def detect_weiqi(img):  # 检测棋子的颜色
    txt = 'black'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    c = Counter(list(threshold.flatten()))
    print(c.most_common())
    if c.most_common()[0][0] != 0:
        txt = 'white'
    return txt, threshold


img = cv2.imread('../data/weiqi.png')

img = cv2.medianBlur(img, 5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)#不行
cv2.imshow('gray', gray)
# cv2.imshow('threshold', threshold)
# cv2.waitKey(0)

# HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=40)#有一些没有检测到
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=10, maxRadius=50)

if circles is None:
    exit(-1)

circles = np.uint16(np.around(circles))
print(circles)

cv2.waitKey(0)
font = cv2.FONT_HERSHEY_SIMPLEX
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    x, y, r = i
    crop_img = img[y - r:y + r, x - r:x + r]
    # 检测围棋
    txt, threshold = detect_weiqi(crop_img)
    print('颜色：', '黑色' if txt == 'black' else '白色')

    cv2.putText(threshold, text=txt, org=(0, 0), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)
    cv2.imshow('threshold', threshold)

    cv2.imshow('crop_img', crop_img)
    cv2.moveWindow('crop_img', x=0, y=img.shape[0])

    cv2.imshow('detected chess', img)
    cv2.moveWindow('detected chess', y=0, x=img.shape[1])

    cv2.waitKey(1500)

cv2.waitKey(0)
cv2.destroyAllWindows()
