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
import string, random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    print('frame.shape:', frame.shape)  # (720, 1280, 3)

    cv2.imshow('frame',frame)

    key = cv2.waitKey(delay=1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite(id_generator() + '.jpg', frame)

cap.release()
cv2.destroyAllWindows()
