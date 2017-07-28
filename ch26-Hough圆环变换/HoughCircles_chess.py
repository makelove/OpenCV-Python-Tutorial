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

img = cv2.imread('../data/weiqi.png')

img = cv2.medianBlur(img, 5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=40)#有一些没有检测到
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=10, maxRadius=50)

circles = np.uint16(np.around(circles))
print(circles)

cv2.waitKey(0)
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected chess', img)
    cv2.moveWindow('detected chess',y=0,x=img.shape[1])
    cv2.waitKey(100)

cv2.waitKey(0)
cv2.destroyAllWindows()
