# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午9:30
# @Author  : play4fun
# @File    : 21.4.3-形状匹配.py
# @Software: PyCharm

"""
21.4.3-形状匹配.py:
函数 cv2.matchShape() 可以帮我们比 两个形状或 廓的相似度。
如果返回值越小， 匹配越好。它是根据 Hu 矩来计算的。文档中对不同的方法有解释。

"""

import cv2
import numpy as np

img1 = cv2.imread('star.jpg', 0)
img2 = cv2.imread('star2.jpg', 0)

ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)

#Hu 矩是归一化中心矩的线性组合
# 之所以 样做是为了能够获取 代表图像的某个特征的矩函数
# 这些矩函数对某些变化如缩放 旋转，  镜像映射  （ 除了 h1） 具有不变形。