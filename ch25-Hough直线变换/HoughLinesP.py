# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-25 上午11:53
"""

import cv2
import numpy as np

img = cv2.imread('../data/sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
print("Len of lines:", len(lines))
print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# cv2.imwrite('houghlines5.jpg',img)
cv2.imshow("houghlines3.jpg", img)
cv2.waitKey(0)
