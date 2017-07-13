# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午3:31
# @Author  : play4fun
# @File    : fast.py
# @Software: PyCharm

"""
fast.py:FAST 特征检测器

效果很好。但是从实时处理的角度来看
这些算法 不够快。
一个最好例子就是 SLAM 同步定位与地图构建
移动机器人 它们的计算资源非常有限。

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('simple.jpg', 0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))

# Print all default params
print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))
cv2.imwrite('fast_true.png', img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
cv2.imwrite('fast_false.png', img3)

#结果如下。第一幅图是使用了 非最大值抑制的结果
# 第二幅没有使用非最大值抑制。