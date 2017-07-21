# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 下午4:11
# @Author  : play4fun
# @File    : draw最大的轮廓.py
# @Software: PyCharm

"""
draw最大的轮廓.py:
"""

import cv2
import numpy as np

img22 = cv2.imread('../data/cards.png')
imgray = cv2.cvtColor(img22, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray', imgray)

#白色背景
ret, threshold = cv2.threshold(imgray, 244, 255, cv2.THRESH_BINARY_INV)#把黑白颜色反转
cv2.imshow('after threshold', threshold)

image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = list()
for i, cnt in enumerate(contours):
    areas.append((i, cv2.contourArea(cnt)))

#
a2 = sorted(areas, key=lambda d: d[1], reverse=True)

for i, are in a2:
    if are < 100:
        continue
    cv2.drawContours(img22, contours, i, (0, 0, 255), 3)
    print(i, are)

    cv2.imshow('drawContours', img22)
    cv2.waitKey(0)

cv2.destroyAllWindows()
