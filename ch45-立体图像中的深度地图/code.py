# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午7:09
# @Author  : play4fun
# @File    : code.py
# @Software: PyCharm

"""
code.py:
下图左侧为原始图像 右侧为深度图像。
如图所示 结果中有很大的噪音。
通过调整 numDisparities 和 blockSize 的值 我们会得到更好的结果。
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('tsukuba_l.png', 0)
imgR = cv2.imread('tsukuba_r.png', 0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL, imgR)

plt.imshow(disparity, 'gray')
plt.show()

