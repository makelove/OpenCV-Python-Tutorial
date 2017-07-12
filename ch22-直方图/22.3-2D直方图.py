# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午10:32
# @Author  : play4fun
# @File    : 22.3-2D直方图.py
# @Software: PyCharm

"""
22.3-2D直方图.py:
一维 是因为 我们只考 了图像的一个特征：灰度值。
但是在 2D 直方图中我们就 考虑  两个图像特征。

对于彩色图像的直方图通常情况下我们  考 每个的颜色
 Hue 和 饱和度 Saturation 。
 根据 两个特征绘制 2D 直方图。

 使用函数 cv2.calcHist() 来 算直方图既简单又方便。如果 绘制 色 直方图的  我们 先  将图像的 色空 从 BGR  换到 HSV。  住   算一维直方图  从 BGR  换到 HSV 。 算 2D 直方图 函数的参数  做如下修改
• channels=[0 1] 因为我们  同时处理 H 和 S 两个  。
• bins=[180 256]H   为 180 S   为 256。
• range=[0 180 0 256]H 的取值范围在 0 到 180 S 的取值范围 在 0 到 256。

"""

import cv2
import numpy as np

img = cv2.imread('../data/home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Numpy 同样提供了绘制 2D 直方图的函数 np.histogram2d()。
# 绘制 1D 直方图时我们使用的是 np.histogram() 。

h, s, v = cv2.split(hsv)

hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]])

pass
