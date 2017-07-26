# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 23:42
# @Author  : play4fun
# @File    : LineSegmentDetector1.py
# @Software: PyCharm

"""
LineSegmentDetector1.py:
"""
import cv2
import numpy as np

# Read gray image
img0 = cv2.imread("pokerQ.jpg")
img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

# Create default parametrization LSD
lsd = cv2.createLineSegmentDetector(0)

# Detect lines in the image
dlines = lsd.detect(img)#TODO 返回什么？
lines = lsd.detect(img)[0]  # Position 0 of the returned tuple are the detected lines

# Draw detected lines in the image
# drawn_img = lsd.drawSegments(img, lines)

#
for dline in dlines[0]:
    x0 = int(round(dline[0][0]))
    y0 = int(round(dline[0][1]))
    x1 = int(round(dline[0][2]))
    y1 = int(round(dline[0][3]))
    cv2.line(img0, (x0, y0), (x1,y1), (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow("LSD", img0)
    cv2.waitKey(1000)

#TODO 最长的直线？

# Show image
# cv2.imshow("LSD", drawn_img)
# cv2.imshow("LSD", img0)
cv2.waitKey(0)
