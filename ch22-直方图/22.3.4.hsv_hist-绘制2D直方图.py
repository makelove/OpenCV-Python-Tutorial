# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-11-8 下午4:44
绘制2D直方图
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/home.jpg')
# cv2.imshow("src", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(hist, interpolation='nearest')
plt.show()
