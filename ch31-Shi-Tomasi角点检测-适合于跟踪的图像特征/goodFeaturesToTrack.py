# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-29 上午7:52

使用 Shi-Tomasi 方法获取图像中 N 个最好的角点

 常情况下  入的应  是灰度图像。然后确定你想 检测到的 点数目。再 置 点的  水平 0 到 1 之 。它代 了 点的最低   低于 个数的所有 点 会 忽略。最 后在 置两个角点之间的最短欧式距离。
 
 所有低于  水平的 点  会 忽略。然后再把合格 点按 点     序排列。
 函数会 用 点   最 的 个 点 排序后的第一个  然后将它   最小 离之内 的 点  删掉。
 按着 样的方式最后 回 N 个最佳 点。
 
 以后会发现这个函数很适合在目标跟踪中使用
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = '../data/corner-detection.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=25, qualityLevel=0.01, minDistance=10)

# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img), plt.show()
