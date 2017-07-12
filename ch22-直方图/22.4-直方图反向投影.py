# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午11:01
# @Author  : play4fun
# @File    : 22.4-直方图反向投影.py
# @Software: PyCharm

"""
22.4-直方图反向投影.py:

直方图反向投影是由 Michael J. Swain 和 Dana H. Ballard 在他们的 文章 Indexing via color histograms 中提出。

 它到底是什么呢 它可以用来做图像分割 或者在图像中找寻我们感兴  的 分。
 简单来  它会 出与 入图像 待搜索 同样大小的图像 其中 的每一个像素值代 了 入图像上对应点属于目标对 的概率。
 用更简单的  来   输出图像中像素值越高(越白) 的点就 可能代表我们 搜索的目标
 在输入图像所在的位置 。
 这是一个直观的解释  。

 直方图投影经常与 camshift 算法等一 使用。



"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Numpy 中的算法

# roi is the object or region of object we need to find
roi = cv2.imread('rose_red.png')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# target is the image we search in
target = cv2.imread('rose.png')

hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])

h, s, v = cv2.split(hsvt)
B = R[h.ravel(), s.ravel()]
B = np.minimum(B, 1)
B = B.reshape(hsvt.shape[:2])

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
B = cv2.filter2D(B, -1, disc)
B = np.uint8(B)
cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)

ret,thresh = cv2.threshold(B,50,255,0)


