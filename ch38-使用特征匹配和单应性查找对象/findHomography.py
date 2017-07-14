# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午5:13
# @Author  : play4fun
# @File    : findHomography.py
# @Software: PyCharm

"""
findHomography.py:联合使用特征提取和 calib3d 模块中的 findHomography 在复杂图像中查找已知对象
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
img1 = cv2.imread('../data/box.png', 0)  # queryImage
img2 = cv2.imread('../data/box_in_scene.png', 0)  # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)
'''
现在我们 置只有存在 10 个以上匹 时才去查找目标 MIN_MATCH_COUNT=10   否则显示 告消息  现在匹 不   
如果找到了 够的匹  我们 提取两幅图像中匹 点的坐标。把它们传 入到函数中 算  变换。一旦我们找到 3x3 的变换矩  就可以使用它将查  图像的四个 点 四个  变换到目标图像中去了。然后再绘制出来。
'''

if len(good) > MIN_MATCH_COUNT:
    # 获取关 点的坐标
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # 第三个参数 Method used to computed a homography matrix. The following methods are possible: #0 - a regular method using all the points
    # CV_RANSAC - RANSAC-based robust method
    # CV_LMEDS - Least-Median robust method
    # 第四个参数取值范围在 1 到 10  绝一个点对的 值。原图像的点经 变换后点与目标图像上对应点的 差 #    差就 为是 outlier
    #  回值中 M 为变换矩 。
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()
    # 获得原图像的高和宽
    h, w = img1.shape
    # 使用得到的变换矩 对原图像的四个   变换 获得在目标图像上对应的坐标
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)
    # 原图像为灰度图
    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
    print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
    matchesMask = None

# 最后我再绘制 inliers 如果能成功的找到目标图像的话  或者匹配的关  点 如果失败。
draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                   singlePointColor=None,
                   matchesMask=matchesMask,  # draw only inliers
                   flags=2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

plt.imshow(img3, 'gray'), plt.show()
# 复杂图像中被找到的目标图像被标记成白色
