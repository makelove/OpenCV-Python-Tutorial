# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 19:19
# @Author  : play4fun
# @File    : 创建图片1.py
# @Software: PyCharm

"""
创建图片1.py:
"""

import numpy as np
import cv2

size = (2560, 1600)
# 全黑.可以用在屏保
black = np.zeros(size)
cv2.imwrite('black.jpg',black)

#white
black[:]=255
cv2.imwrite('white.jpg',black)