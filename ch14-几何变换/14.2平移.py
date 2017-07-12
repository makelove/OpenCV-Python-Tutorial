# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午12:21
# @Author  : play4fun
# @File    : 平移.py
# @Software: PyCharm

"""
平移.py:平移就是将对 换一个位置。如果你 沿 (x, y) 方向移动
移动的距离 是 (tx,ty)
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    # 获取每一帧
    ret, frame = cap.read()

    #  换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #  定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 对原图像和掩模 进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(0)  # & 0xFF
    if k == ord('q'):
        break
# 关 窗口
cv2.destroyAllWindows()
