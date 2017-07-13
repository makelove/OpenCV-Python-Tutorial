# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午10:33
# @Author  : play4fun
# @File    : inpaint.py
# @Software: PyCharm

"""
inpaint.py:
算法
1.基于快速行进算法cv2.INPAINT_TELEA
2.基于流体动力学并使用了偏微分方程。基本原理是启发式的    cv2.INPAINT_NS
"""

import numpy as np
import cv2

img = cv2.imread('messi_2.jpg')
mask = cv2.imread('mask2.png', 0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
