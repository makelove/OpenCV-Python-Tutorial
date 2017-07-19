# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 下午12:42
# @Author  : play4fun
# @File    : test_cvwm_images.py
# @Software: PyCharm

"""
test_cvwm_images.py:
# show 多张相片
"""

import cv2
import numpy as np
import os
import errno
from opencv_windows_management import opencv_windows_management

cvwm = opencv_windows_management()

path = '../../data/messi5.jpg'
if not os.path.exists(path):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # 包括图像的 alpha 通道
print(img.shape)
# cv2.imshow('src', img)
cvwm.add('src', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray', gray)
cvwm.add('gray', gray)

ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cvwm.add('thresh1', thresh1)

cvwm.show()

cv2.waitKey(0)
