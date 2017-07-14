# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午3:38
# @Author  : play4fun
# @File    : brief.py
# @Software: PyCharm

"""
brief.py:
算法使用的是已经平滑后的图像

非常重要的一点是 BRIEF 是一种特征描述符 它不提供查找特征的方法。 所以我们不得不使用其他特征检测器 比如 SIFT 和 SURF 等。
原始文献推荐 使用 CenSurE 特征检测器  种算法很快。而且 BRIEF 算法对 CenSurE 关键点的描述效果 比 SURF 关键点的描述更好。

简单来  BRIEF 是一种对特征点描述符运算和匹 的快速方法。 这种算法可以实现很高的识别率，除非出现平面内的大旋 。

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/blox.jpg', 0)

# Initiate FAST detector
star = cv2.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# find the keypoints with STAR
kp = star.detect(img, None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print(brief.descriptorSize())
print(des.shape)
