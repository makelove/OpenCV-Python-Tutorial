# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 12:33
# @Author  : play4fun
# @File    : minAreaRect-旋转矩形.py
# @Software: PyCharm

"""
minAreaRect-旋转矩形.py:
"""

import cv2
import numpy as np

img = cv2.imread('../data/lightning.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

image, contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
print('len(contours)', len(contours))
cnt = contours[0]

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

cv2.imshow('fd', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
