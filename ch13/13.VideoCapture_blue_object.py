# -*- coding: utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while (1):
    # 获取每一帧
    ret, frame = cap.read()
    # 换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 定蓝色的 值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 根据 值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 对原图像和掩模位 算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
# 关 窗口
cv2.destroyAllWindows()
