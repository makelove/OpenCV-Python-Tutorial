# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午2:23
# @Author  : play4fun
# @File    : sift.py
# @Software: PyCharm

"""
sift.py:尺度不变特征变换

关键点 极值点 定位

"""

import cv2
import numpy as np

img = cv2.imread('../data/home.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, img)

# 计算关键点描述符
# 使用函数 sift.compute() 来 计算 些关键点的描述符。例如
# kp, des = sift.compute(gray, kp)
kp, des = sift.detectAndCompute(gray,None)

cv2.imwrite('sift_keypoints.jpg', img)
cv2.imshow('sift_keypoints.jpg', img)
cv2.waitKey(0)
