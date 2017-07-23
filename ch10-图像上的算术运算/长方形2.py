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


def get_euler_distance(pt1, pt2):
    return ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5


img22 = cv2.imread('subtract2.jpg')

# src_pts = np.array([[8, 136], [415, 52], [420, 152], [14, 244]], dtype=np.float32)

src_pts = np.array([[[97, 390], [210, 373], [183, 199], [69, 214]]], dtype=np.float32)
# src_pts = np.array([[ [210, 373], [183, 199], [69, 214],[97, 390]]], dtype=np.float32)

width = get_euler_distance(src_pts[0][0], src_pts[0][1])
height = get_euler_distance(src_pts[0][0], src_pts[0][3])

dst_pts = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

M = cv2.getPerspectiveTransform(src_pts, dst_pts)
warp = cv2.warpPerspective(img22, M, (int(width), int(height)))

warp=cv2.flip(warp,flipCode=1)

cv2.imshow('src', img22)
cv2.imshow('warp', warp)
# cv2.imwrite('crop0.jpg',warp)
cv2.waitKey(0)
