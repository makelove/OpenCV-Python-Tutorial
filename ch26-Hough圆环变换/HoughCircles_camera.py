# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 13:47
# @Author  : play4fun
# @File    : HoughCircles_camera.py
# @Software: PyCharm

"""
HoughCircles_camera.py:

用围棋-棋子来测试
"""

import cv2
import numpy as np
from skimage.measure import compare_mse as mse
import string, random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


cap = cv2.VideoCapture(0)

# ret = cap.set(3, 640)
# ret = cap.set(4, 480)

# margin = 60
margin = 30


def draw_line_rectangle(frame, margin):
    rows, cols, ch = frame.shape  # (720, 1280, 3)
    half = int(cols / 2)
    # 中间
    cv2.line(frame, (half, 0), (half, rows), (0, 0, 255), 2)

    # margin = 40
    # 左边
    up_left1 = (margin, margin)  # 左上点
    down_right1 = (cols - margin, rows - margin)  # 右下点
    # print(up_left, down_right)
    cv2.rectangle(frame, up_left1, down_right1, (0, 255, 0), 3)


ret, temp = cap.read()
tm = 0
while cap.isOpened():
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord('s'):
        cv2.imwrite(id_generator() + '.jpg', frame2)

    # Capture frame-by-frame
    ret, frame = cap.read()
    m = mse(cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY), cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    print('mse', m, '----\n')
    if abs(m - tm) < 2:  # 静止画面，不用重复计算
        continue
    else:
        temp = frame.copy()
        tm = m
    #
    # print(margin,frame.shape[0] - margin, margin,frame.shape[1] - margin)#40 680 40 1240
    frame2 = frame[margin:frame.shape[0] - margin, margin:frame.shape[1] - margin]  # .copy()
    # cv2.imshow('frame2', frame2)

    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=10, maxRadius=40)

    # circles = circles1[0, :, :]  # 提取为二维
    # circles = np.uint16(np.around(circles1))
    print(circles)

    cimg = frame2
    if circles is not None:
        for i in circles[0, :]:
            # for i in circles[:]:
            # draw the outer circle
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    # cv2.imshow('detected circles', cimg)

    draw_line_rectangle(frame, margin)
    cv2.imshow("houghlines", frame)
    # cv2.imwrite('frame3.jpg', frame[margin:frame.shape[0] - margin, margin:frame.shape[1] - margin])

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
