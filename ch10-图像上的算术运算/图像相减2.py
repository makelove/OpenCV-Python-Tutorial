# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 上午10:48
# @Author  : play4fun
# @File    : 图像相减2.py
# @Software: PyCharm

"""
图像相减2.py:
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img1=cv2.imread('subtract1.jpg')
img1 = cv2.imread('subtract1.jpg', 0)  # 灰度图
# img2=cv2.imread('subtract2.jpg')
img2 = cv2.imread('subtract2.jpg', 0)

cv2.imshow('subtract1', img1)
cv2.imshow('subtract2', img2)

#
st = cv2.subtract(img2, img1)
# st = cv2.subtract(img1, img2)#相反
st[st<=5]=0 #把小于20的像素点设为0

cv2.imshow('after subtract', st)


'''
# 直方图，看看大部分像素集中在哪个区域
# plt.plot(st)
pxs = st.ravel()
pxs=[x for x in pxs if x>5]#20,10
plt.hist(pxs, 256, [0, 256])
plt.show()
'''

# 效果好一点
# ret,threshold=cv2.threshold(st,0, 127, cv2.THRESH_BINARY)
ret, threshold = cv2.threshold(st, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('after threshold', threshold)

cv2.waitKey(0)
