#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-28 下午7:27
"""

import cv2
import numpy as np
# filename = '../data/chessboard-3.png'
filename = '../data/corner-detection.jpg'

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#输入图像必 是 float32 最后一个参数在 0.04 到 0.05 之间
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()