# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 下午7:24
# @Author  : play4fun
# @File    : VideoCaptureOnePicture.py
# @Software: PyCharm

"""
VideoCaptureOnePicture.py:
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    print('frame.shape:',frame.shape)#(720, 1280, 3)

    cv2.imwrite('from_camera1.jpg',frame)
