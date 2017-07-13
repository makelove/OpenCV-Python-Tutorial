# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-25 上午11:42
"""

import cv2
import numpy as np

img = cv2.imread('../data/sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
edges = cv2.Canny(gray, 10, 50, apertureSize=3)
cv2.imshow("edges", edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
print("Len of lines:", len(lines))
# print lines

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# cv2.imwrite('houghlines3.jpg',img)
cv2.imshow("houghlines3.jpg", img)
cv2.waitKey(0)
