# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 下午12:03
# @Author  : play4fun
# @File    : 画圆圈.py
# @Software: PyCharm

"""
画圆圈.py:随机覆盖，不同颜色，
"""

import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
