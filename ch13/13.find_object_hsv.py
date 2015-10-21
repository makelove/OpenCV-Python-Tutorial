# -*- coding: utf-8 -*-
import cv2
import numpy as np

#wrong
# green=np.uint8([0,255,0])
# print green
# hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print hsv_green


#scn (the number of channels of the source),
#i.e. self.img.channels(), is neither 3 nor 4.
#
#depth (of the source),
#i.e. self.img.depth(), is neither CV_8U nor CV_32F.
# 所以不能用 [0,255,0] 而 用 [[[0,255,0]]]
#的三层括号应 分别对应于 cvArray cvMat IplImage
green=np.uint8([[[0,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
#[[[60 255 255]]]