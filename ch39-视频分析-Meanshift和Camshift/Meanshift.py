# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午5:27
# @Author  : play4fun
# @File    : Meanshift.py
# @Software: PyCharm

"""
Meanshift.py:

问题：我们的窗口的大小是固 定的
而汽车由远及近 在视觉上 是一个 渐变大的过程
固定的窗口是不 合适的。所以我们需要根据目标的大小和角度来对窗口的大小和角度进行修订

http://docs.opencv.org/3.2.0/db/df8/tutorial_py_meanshift.html
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('../data/slow.flv')

# take first frame of the video
ret, frame = cap.read()
# setup initial location of window
r, h, c, w = 250, 90, 400, 125  # simply hardcoded the values
track_window = (c, r, w, h)
# set up the ROI for tracking
roi = frame[r:r + h, c:c + w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 将低亮度的值忽略掉
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x, y, w, h = track_window
        print(track_window)
        img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv2.imshow('img2', img2)


        k = cv2.waitKey(60)  # & 0xff
        if k == 27:
            break
            # else:
            #     cv2.imwrite(chr(k) + ".jpg", img2)
    else:
        break
cv2.destroyAllWindows()
cap.release()
#不正常
