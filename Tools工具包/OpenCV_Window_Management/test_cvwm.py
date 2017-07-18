# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 上午10:19
# @Author  : play4fun
# @File    : test_cvwm.py
# @Software: PyCharm

"""
test_cvwm.py:
"""
import cv2
import numpy as np
import opencv_windows_management as cvwm

# show 多张相片

cv2.namedWindow()
cv2.resize()
cv2.moveWindow()
cv2.imshow()

cv2.waitKey(0)


#
class Windows():
    def __init__(self):
        self.windows = list()
    pass

    def imshow(name, img, style=grid, ):
        cv2.namedWindow(winname=name, flags=cv2.WINDOW_AUTOSIZE)
        img2 = img.copy()

        for window in windows:
            cv2.resize()
            cv2.moveWindow()
            cv2.imshow()
