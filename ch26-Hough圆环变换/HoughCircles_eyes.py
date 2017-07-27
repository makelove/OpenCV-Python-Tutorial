# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 10:57
# @Author  : play4fun
# @File    : HoughCircles_eyes.py
# @Software: PyCharm

"""
HoughCircles_eyes.py:

http://blog.csdn.net/on2way/article/details/47028969

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('eye-color-blue-z-c-660x440.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像

plt.subplot(121), plt.imshow(gray, 'gray')
plt.xticks([]), plt.yticks([])
# hough transform   #规定检测的圆的最大最小半径，不能盲目的检测，否侧浪费时间空间。
# circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,100, param1=100, param2=30, minRadius=200, maxRadius=300)
circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=100, maxRadius=200)  # 把半径范围调小点，检测内圆,瞳孔
circles = circles1[0, :, :]  # 提取为二维
circles = np.uint16(np.around(circles))  # 四舍五入，取整
for i in circles[:]:
    cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)  # 画圆
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心

plt.subplot(122), plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()
