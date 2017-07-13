# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 下午12:01
# @Author  : play4fun
# @File    : HoughLinesP_camera.py
# @Software: PyCharm

"""
HoughLinesP_camera.py:
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# ret = cap.set(3, 640)
# ret = cap.set(4, 480)

# while (True):
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    # img = cv2.imread('../data/sudoku.jpg')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    if lines is None:
        continue
    print("Len of lines:", len(lines))
    print(lines)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # cv2.imwrite('houghlines5.jpg',img)
    cv2.imshow("houghlines3.jpg", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
