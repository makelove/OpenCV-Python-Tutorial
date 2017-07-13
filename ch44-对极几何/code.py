# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午6:57
# @Author  : play4fun
# @File    : code.py
# @Software: PyCharm

"""
code.py:多视角几何基础，极点 极线 对极约束 对极平面

在我们使用针孔相机时 我们会丢失大量重要的信息
 比如 图像的深度  或者 图像上的点和摄像机的距离
因为这是一个从 3D 到 2D 的转换。
重要的问题：
 使用这样的摄像机我们能否计算出深度信息呢？
  答案 就是使用多个相机。
  我们的眼睛就是这样工作的 使用两个摄像机 两个眼睛
称为立体视角

三角测量

本征矩阵 E 和基础矩阵 F

点越多越好 可以使用 RANSAC 算法得到更加稳定的结果

使用 SIFT 描述符 FLANN 匹配器和比值检测
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


# 找到极线
def drawlines(img1, img2, lines, pts1, pts2):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r, c = img1.shape
    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        x0, y0 = map(int, [0, -r[2] / r[1]])
        x1, y1 = map(int, [c, -(r[2] + r[0] * c) / r[1]])
        img1 = cv2.line(img1, (x0, y0), (x1, y1), color, 1)
        img1 = cv2.circle(img1, tuple(pt1), 5, color, -1)
        img2 = cv2.circle(img2, tuple(pt2), 5, color, -1)
    return img1, img2


img1 = cv2.imread('myleft.jpg', 0)  # queryimage # left image
img2 = cv2.imread('myright.jpg', 0)  # trainimage # right image
sift = cv2.SIFT()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
good = []
pts1 = []
pts2 = []
# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.8 * n.distance:
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)
        # 匹配点列表，用它来计算【基础矩阵】
        pts1 = np.int32(pts1)
        pts2 = np.int32(pts2)
        F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_LMEDS)
        # We select only inlier points
        pts1 = pts1[mask.ravel() == 1]
        pts2 = pts2[mask.ravel() == 1]
        # 从两幅图像中计算并绘制极线
        # Find epilines corresponding to points in right image (second image) and
        # drawing its lines on left image
        lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F)
        lines1 = lines1.reshape(-1, 3)
        img5, img6 = drawlines(img1, img2, lines1, pts1, pts2)
        # Find epilines corresponding to points in left image (first image) and
        # drawing its lines on right image
        lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1, 1, 2), 1, F)
        lines2 = lines2.reshape(-1, 3)
        img3, img4 = drawlines(img2, img1, lines2, pts2, pts1)
        plt.subplot(121), plt.imshow(img5)
        plt.subplot(122), plt.imshow(img3)
        plt.show()

#从上图可以看出所有的极线都汇聚以图像外的一点  这个点就是极点。
# 为了得到更好的结果 我们应 使用分辨率比较高的图像和 non-planar 点