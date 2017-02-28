#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-23 下午12:56
"""

import cv2
import numpy as np
img = cv2.imread('../data/star.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
# ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(thresh, 1, 2)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt)
print M