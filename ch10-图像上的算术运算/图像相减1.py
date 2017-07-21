# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 上午10:48
# @Author  : play4fun
# @File    : 图像相减1.py
# @Software: PyCharm

"""
图像相减1.py:
"""

import cv2
import numpy as np

# img1=cv2.imread('subtract1.jpg')
img1=cv2.imread('subtract1.jpg',0)#灰度图
# img2=cv2.imread('subtract2.jpg')
img2=cv2.imread('subtract2.jpg',0)

cv2.imshow('subtract1',img1)
cv2.imshow('subtract2',img2)

#
st=img2-img1
# st=img1-img2#相反
cv2.imshow('after subtract',st)

#效果好一点
# ret,threshold=cv2.threshold(st,0, 127, cv2.THRESH_BINARY)
ret,threshold=cv2.threshold(st, 50,255, cv2.THRESH_BINARY)
cv2.imshow('after threshold', threshold)


cv2.waitKey(0)