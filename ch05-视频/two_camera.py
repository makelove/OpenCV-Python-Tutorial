# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 00:19
# @Author  : play4fun
# @File    : two_camera.py
# @Software: PyCharm

"""
two_camera.py:
"""

import cv2

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
ret = cap0.set(3, 320)
ret = cap0.set(4, 240)
ret = cap1.set(3, 320)
ret = cap1.set(4, 240)

while cap0.isOpened() and cap1.isOpened():
    ret, frame0 = cap0.read()
    ret, frame1 = cap1.read()

    cv2.imshow('frame0', frame0)
    cv2.imshow('frame1', frame1)
    cv2.moveWindow('frame1', x=frame0.shape[1], y=0)

    key = cv2.waitKey(delay=10)
    if key == ord("q"):
        break

# When everything done, release the capture
cap0.release()
cap1.release()
cv2.destroyAllWindows()
