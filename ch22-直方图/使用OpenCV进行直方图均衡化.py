# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午10:16
# @Author  : play4fun
# @File    : 使用OpenCV进行直方图均衡化.py
# @Software: PyCharm

"""
使用OpenCV进行直方图均衡化.py:
"""
import cv2
import numpy as np

img = cv2.imread('wiki.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))  # stacking images side-by-side
cv2.imwrite('res.png', res)

'''
当直方图中的数据 中在某一个灰度值范围内时 直方图均 化很有用。 但是如果像素的变化很大 而且占据的灰度范围 常广时 例如 既有很亮的 像素点又有很暗的像素点时
'''