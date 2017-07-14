# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午6:21
# @Author  : play4fun
# @File    : 42.2.1-设置-findChessboardCorners.py
# @Software: PyCharm

"""
42.2.1-设置-findChessboardCorners.py:

径向畸变和切想畸变
摄像机的内部和外部参数。 内部参数是摄像机特异的。它包括的信息有焦 ( fx, fy) 光学中心 (cx, cy)  等。 也 称为摄像机矩阵。它完全取决于摄像机自  只需要计算一次 以后就可以已知使用了。

至少需要10张图案模式来进行摄像机标定
3D 点 称为对象点， 2D 图像点 称为图像点

除了使用棋盘之外 我们 可以使用环形格子
使用函数 cv2.findCirclesGrid() 来找图案。
据说使用环形格子只需要很少的图像 就可以了。

"""

import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
images = glob.glob('../data/left*.jpg')
images += glob.glob('../data/right*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)
cv2.destroyAllWindows()
