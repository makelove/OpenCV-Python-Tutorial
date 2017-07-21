# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 下午6:12
# @Author  : play4fun
# @File    : 长方形1.py
# @Software: PyCharm

"""
长方形1.py:
[[[183 199]]
 [[ 69 214]]
 [[ 97 390]]
 [[210 373]]]

"""
import cv2
import numpy as np

img22 = cv2.imread('subtract2.jpg')

# src_pts = np.array([[8, 136], [415, 52], [420, 152], [14, 244]], dtype=np.float32)

src_pts = np.array([[[97, 390], [210, 373], [183, 199], [69, 214]]], dtype=np.float32)

dst_pts = np.array([[0, 0], [50, 0], [50, 100], [0, 100]], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_pts, dst_pts)
warp = cv2.warpPerspective(img22, M, (50, 100))

cv2.imshow('src', img22)
cv2.imshow('warp', warp)
cv2.waitKey(0)
