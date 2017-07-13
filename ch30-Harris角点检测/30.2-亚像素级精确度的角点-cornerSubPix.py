# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-29 上午7:47

最大精度的角点检测

首先我们 找到 Harris 角点
 然后将角点的重心传给这个函数进行修正。
 Harris 角点用红色像素标出 
 绿色像素是修正后的像素。
 在使用 个函数是我们 定义一个爹代停止条件。
 当 代次数 到或者精度条件满 后 代就会停止。
 我们同样需要定义进行角点搜索的邻域大小。
"""

import cv2
import numpy as np

filename = '../data/chessboard-2.png'
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
dst = np.uint8(dst)

# find centroids
# connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
# OutputArray centroids, int connectivity=8, int ltype=CV_32S)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
# zeroZone – Half of the size of the dead region in the middle of the search zone
# over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
# indicates that there is no such a size.
# 返回值由 点坐标组成的一个数组 而 图像
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
# Now draw them
res = np.hstack((centroids, corners))
# np.int0 可以用来省略小数点后的数字，非四舍五入
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]
img[res[:, 3], res[:, 2]] = [0, 255, 0]

# cv2.imwrite('subpixel5.png',img)
cv2.imshow('subpixel5.png', img)
cv2.waitKey(0)
