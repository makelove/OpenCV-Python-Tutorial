# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午12:31
# @Author  : play4fun
# @File    : 14.2平移-2.py
# @Software: PyCharm

"""
14.2平移-2.py:
http://docs.opencv.org/3.2.0/da/d6e/tutorial_py_geometric_transformations.html
函数 cv2.warpAffine() 的第三个参数的是 出图像的大小 ，它的格式 应 是图像的(宽,高) 。
图像的宽对应的是列数, 高对应的是行数。
"""

import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
