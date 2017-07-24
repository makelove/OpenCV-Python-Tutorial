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

# 定蓝色的阈值
# lower = np.array([110, 50, 50])
# upper = np.array([130, 255, 255])

#黄色-乒乓球
lower = np.array([20, 100, 100])
upper = np.array([30, 255, 255])

# 黑色
# lower_black = np.array([0, 0, 0])
# upper_black = np.array([180, 255, 30])

while True:
    # 获取每一帧
    ret, frame = cap.read()
    # 换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower, upper)
    # mask = cv2.inRange(hsv, lower_black, upper_black)
    # 对原图像和掩模位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', frame)
    cv2.moveWindow('frame', x=0, y=0)  # 原地
    cv2.imshow('mask', mask)
    cv2.moveWindow('mask', x=frame.shape[1], y=0)#右边
    cv2.imshow('res', res)
    cv2.moveWindow('res', y=frame.shape[0], x=0)#下边

    k = cv2.waitKey(1)  # & 0xFF
    if k == ord('q'):
        break
# 关闭窗口
cap.release()
cv2.destroyAllWindows()
