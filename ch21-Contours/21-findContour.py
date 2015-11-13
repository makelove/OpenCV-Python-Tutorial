# -*- coding: utf-8 -*-

import numpy as np
import cv2

# im = cv2.imread('test.jpg')#
# im = cv2.imread('../data/black-white-rect.png')#contour.jpg #
im = cv2.imread('../data/chessboard.jpeg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,0,25,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print "contours size: ", len(contours)
#img = cv2.drawContour(img, contours, -1, (0,255,0), 3)

img = cv2.drawContours(image, contours, 3, (255,0,0), 3)

cv2.namedWindow("contour.jpg",0)
cv2.imshow("contour.jpg",img)
cv2.waitKey(0)