# -*- coding: utf-8 -*-
import cv2
import numpy as np

'''
物体跟踪

• 从视频中获取每一帧图像
• 将图像转换到 HSV 空间
• 设置 HSV 阈值到蓝色范围。
• 获取蓝色物体 当然我们 可以做其他任何我们想做的事 
比如 在蓝色 物体周围画一个圈。


当你学习了【轮廓】之后 你就会学到更多 相关知识
那是你就可以找到物体的重心 并根据重心来跟踪物体
仅仅在摄像头前挥挥手就可以画出同的图形，或者其他更有趣的事。
'''

cap = cv2.VideoCapture(0)
ret = cap.set(3, 640)
ret = cap.set(4, 480)
while True:
    # 获取每一帧
    ret, frame = cap.read()
    # 换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 黑色
    # lower_black = np.array([0, 0, 0])
    # upper_black = np.array([180, 255, 30])

    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # mask = cv2.inRange(hsv, lower_black, upper_black)
    # 对原图像和掩模位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(1)  # & 0xFF
    if k == ord('q'):
        break
# 关闭窗口
cv2.destroyAllWindows()
