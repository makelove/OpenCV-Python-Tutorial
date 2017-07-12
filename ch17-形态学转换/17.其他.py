# -*- coding: utf-8 -*-


import cv2
import numpy as np

img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)

kernel = np.ones((5, 5), np.uint8)

# 开运算：先腐蚀再膨胀就叫做开运算。就像我们上 介绍的 样， 它 用来，去噪声。
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('opening', opening)
cv2.moveWindow('opening', x=img.shape[1], y=0)

# 闭运算
# 先膨胀再腐 。它经常 用来填充前景物体中的小洞 或者前景物体上的小黑点。
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.moveWindow('closing', x=img.shape[1] * 2, y=0)

# 形态学梯度
# 其实就是一幅图像膨胀与腐 的差别。
# 结果看上去就像前景物体的 廓。
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)
cv2.moveWindow('gradient', x=img.shape[1] * 3, y=0)

# 礼帽
# 原始图像与  开运算之后得到的图像的差。
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', tophat)
cv2.moveWindow('tophat', x=img.shape[1] * 4, y=0)

# 黑帽  进行闭运算之后得到的图像与原始图像的差
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', blackhat)
cv2.moveWindow('blackhat', x=img.shape[1] * 5, y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
结构化元素
在前 的例子中我们使用 Numpy 构建了结构化元素 它是正方形的。
但 有时我们 需要 构建一个椭圆形/圆形的核。
为了实现 这种需求 ，提供了 OpenCV 函数 cv2.getStructuringElement()。
你只  告诉 他 你需要的核的形状和大小。
# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
'''
