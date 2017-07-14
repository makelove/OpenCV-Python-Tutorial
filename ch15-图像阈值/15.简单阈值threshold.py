# -*- coding: utf-8 -*-
'''
简单阈值
像素值高于阈值时 我们给这个像素 赋予一个新值， 可能是白色 ，
 否则我们给它赋予另外一种颜色， 或是黑色 。
 这个函数就是 cv2.threshhold()。
 这个函数的第一个参数就是原图像
 原图像应 是灰度图。
 第二个参数就是用来对像素值进行分类的阈值。
 第三个参数 就是当像素值高于， 有时是小于  阈值时应该被赋予的新的像素值。
 OpenCV 提供了多种不同的阈值方法 ， 是由第四个参数来决定的。
  些方法包括
• cv2.THRESH_BINARY
• cv2.THRESH_BINARY_INV • cv2.THRESH_TRUNC
• cv2.THRESH_TOZERO
• cv2.THRESH_TOZERO_INV
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('grey-gradient.jpg', 0)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
