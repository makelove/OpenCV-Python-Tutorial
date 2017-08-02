# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 10:53
# @Author  : play4fun
# @File    : test_camera.py
# @Software: PyCharm

"""
test_camera.py:
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)  # 支持读取摄像头
ret = cap.set(3, 640)
ret = cap.set(4, 480)

plt.ion()
while cap.isOpened():
    ret, frame = cap.read()
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show()
    # plt.show(block=False)#可选
    plt.pause(0.1)
# plt.show()
