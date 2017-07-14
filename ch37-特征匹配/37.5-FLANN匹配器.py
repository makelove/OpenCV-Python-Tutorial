# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午4:22
# @Author  : play4fun
# @File    : 37.5-FLANN匹配器.py
# @Software: PyCharm

"""
37.5-FLANN匹配器.py:
FLANN 是快速最近邻搜索包 Fast_Library_for_Approximate_Nearest_Neighbors 的简称。
它是一个对大数据集和高维特征进行最近邻搜索的算法的集合
 而且这些算法 已经被优化 了。
 在面对大数据集时它的效果 好于 BFMatcher

"""



import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('../data/box.png', 0)  # queryImage
img2 = cv2.imread('../data/box_in_scene.png', 0)  # trainImage

# Initiate SIFT detector
# sift = cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)  # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=0)

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

plt.imshow(img3, ), plt.show()
