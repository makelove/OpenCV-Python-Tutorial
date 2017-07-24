# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 下午5:20
# @Author  : play4fun
# @File    : 图像相减_camera.py
# @Software: PyCharm

"""
图像相减_camera.py:
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret = cap.set(3, 640)
ret = cap.set(4, 480)

cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
cap.read()
'''
cal=[cap.read()[1] for x in range(20)]

#mean 直接的加减是不行的
# bgimg0=np.mean(np.sum(cal))
# bgimg0=np.average(cal)
# bgimg0=np.mean(cal)
nps1=sum(cal)
mean1=nps1/len(cal)
# mean1[mean1<0]=0
# mean1[mean1>255]=255
cv2.imshow('bgimg', mean1)
cv2.waitKey(0)
exit(3)
'''

frame_no = 100
# cap.set(1, frame_no)#第10帧
ret, bgimg0 = cap.read()  # 背景
bgimg = cv2.cvtColor(bgimg0, cv2.COLOR_BGR2GRAY)
cv2.imshow('bgimg' + str(frame_no), bgimg0)

while cap.isOpened():
    ret, frame = cap.read()  # TODO 图像稳定
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #
    st = cv2.subtract(gray, bgimg)
    # st = cv2.subtract(img1, img2)#相反
    # st[st <= 5] = 0  # 把小于20的像素点设为0

    ret, threshold = cv2.threshold(st, 50, 255, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("contours size: ", len(contours))

    # img = cv2.drawContours(st, contours, -1, (0, 0, 0), 13)
    img = cv2.drawContours(st, contours, -1, (255, 255, 255), 3)
    #
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 200:
            continue

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # TODO 对比前几/十几帧，新放一张扑克，知道是那张
    # 等待图像稳定，不放牌后，再计算


    cv2.imshow("frame", frame)
    cv2.imshow("subtract", img)
    cv2.moveWindow("subtract", y=bgimg.shape[0], x=0)
    cv2.imshow('threshold', threshold)
    cv2.moveWindow("threshold", x=bgimg.shape[1], y=0)

    key = cv2.waitKey(delay=1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite('poker-threshold.jpg', threshold)

cv2.destroyAllWindows()
