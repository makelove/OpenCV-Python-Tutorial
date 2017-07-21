# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 上午10:48
# @Author  : play4fun
# @File    : 图像相减2.py
# @Software: PyCharm

"""
图像相减2.py:
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img1=cv2.imread('subtract1.jpg')
img1 = cv2.imread('subtract1.jpg', 0)  # 灰度图
# img2=cv2.imread('subtract2.jpg')
# img2 = cv2.imread('subtract2.jpg', 0)
img22 = cv2.imread('subtract2.jpg')
img2 = cv2.cvtColor(img22, cv2.COLOR_BGR2GRAY)

# cv2.imshow('subtract1', img1)
# cv2.imshow('subtract2', img2)

#
st = cv2.subtract(img2, img1)
# st = cv2.subtract(img1, img2)#相反
st[st <= 5] = 0  # 把小于20的像素点设为0

# cv2.imshow('after subtract', st)

'''
# 直方图，看看大部分像素集中在哪个区域
# plt.plot(st)
pxs = st.ravel()
pxs=[x for x in pxs if x>5]#20,10
plt.hist(pxs, 256, [0, 256])
plt.show()
'''

# 效果好一点
# ret,threshold=cv2.threshold(st,0, 127, cv2.THRESH_BINARY)
ret, threshold = cv2.threshold(st, 50, 255, cv2.THRESH_BINARY)
# cv2.imshow('after threshold', threshold)

image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = list()
for i, cnt in enumerate(contours):

    areas.append((i, cv2.contourArea(cnt)))

#
a2 = sorted(areas, key=lambda d: d[1], reverse=True)

'''
for i,are in a2:
    if are <100:
        continue
    cv2.drawContours(img22, contours, i, (0, 0, 255), 3)
    print(i,are)

    cv2.imshow('drawContours',img22)
    cv2.waitKey(0)
# cv2.destroyAllWindows()
'''

# TODO 截取原图，把长方形纠正
cnt = contours[0]
print(cnt)
hull = cv2.convexHull(cnt)
epsilon = 0.001 * cv2.arcLength(hull, True)
simplified_cnt = cv2.approxPolyDP(hull, epsilon, True)

epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
print(approx)
cv2.drawContours(img22, [approx], 0, (255, 0, 0), 3)
cv2.imshow('approxPolyDP', img22)
cv2.waitKey(0)
exit(3)

# findHomography(srcPoints, dstPoints, method=None, ransacReprojThreshold=None, mask=None, maxIters=None, confidence=None)
# H = cv2.findHomography(srcPoints=cnt.astype('single'), dstPoints=np.array([[[0., 0.]], [[2150., 0.]], [[2150., 2800.]], [[0., 2800.]]]))
# M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)


# now that we have our screen contour, we need to determine
# the top-left, top-right, bottom-right, and bottom-left
# points so that we can later warp the image -- we'll start
# by reshaping our contour to be our finals and initializing
# our output rectangle in top-left, top-right, bottom-right,
# and bottom-left order
pts = approx.reshape(4, 2)
rect = np.zeros((4, 2), dtype="float32")

# the top-left point has the smallest sum whereas the
# bottom-right has the largest sum
s = pts.sum(axis=1)
rect[0] = pts[np.argmin(s)]
rect[2] = pts[np.argmax(s)]

# compute the difference between the points -- the top-right
# will have the minumum difference and the bottom-left will
# have the maximum difference
diff = np.diff(pts, axis=1)
rect[1] = pts[np.argmin(diff)]
rect[3] = pts[np.argmax(diff)]

# multiply the rectangle by the original ratio
ratio = image.shape[0] / 300.0
rect *= ratio


# now that we have our rectangle of points, let's compute
# the width of our new image
(tl, tr, br, bl) = rect
widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

# ...and now for the height of our new image
heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

# take the maximum of the width and height values to reach
# our final dimensions
maxWidth = max(int(widthA), int(widthB))
maxHeight = max(int(heightA), int(heightB))

# construct our destination points which will be used to
# map the screen to a top-down, "birds eye" view
dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], dtype="float32")

# calculate the perspective transform matrix and warp
# the perspective to grab the screen
M = cv2.getPerspectiveTransform(rect, dst)
warp = cv2.warpPerspective(img22, M, (maxWidth, maxHeight))

# final_image = cv2.warpPerspective(img22, H, (2150, 2800))

cv2.imshow('final_image', warp)
cv2.waitKey(0)
