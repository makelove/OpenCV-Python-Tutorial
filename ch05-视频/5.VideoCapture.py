# -*- coding: utf-8 -*-
"""
Created on Fri Jan 3 21:06:22 2014

@author: duan
 """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# while (True):
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    # if cv2.waitKey(1) & 0xFF == ord('q'):#不行
    #     break
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
