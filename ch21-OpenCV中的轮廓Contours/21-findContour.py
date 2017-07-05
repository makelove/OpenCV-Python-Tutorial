# -*- coding: utf-8 -*-

import numpy as np
import cv2

# im = cv2.imread('test.jpg')#
# im = cv2.imread('poker5hearts.jpg')#
# im = cv2.imread('../data/black-white-rect.png')#contour.jpg #
im = cv2.imread('../data/chessboard.jpeg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imshow("imgray", imgray)

#需要注意的是cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图）
# 所以读取的图像要先转成灰度的，再转成二值图
# ret, thresh = cv2.threshold(imgray, 0, 25, 0)
# ret, thresh = cv2.threshold(imgray, 0, 100, 0)
ret, thresh = cv2.threshold(src=imgray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)#src, thresh, maxval, type

cv2.imshow("thresh", thresh)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("contours size: ", len(contours))

img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
# img = cv2.drawContours(im, contours, 3, (255, 0, 0), 3)

cv2.namedWindow("contour.jpg", 0)
cv2.imshow("contour.jpg", img)
cv2.waitKey(0)
