# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 下午4:51
# @Author  : play4fun
# @File    : 斑点检测SimpleBlobDetector.py
# @Software: PyCharm

"""
斑点检测SimpleBlobDetector.py:
https://www.learnopencv.com/blob-detection-using-opencv-python-c/

特别要注意，默认检测黑色点，如果要检测白色的点请设置bycolor为true，并且color数值是255.


斑点通常是指与周围有着颜色和灰度差别的区域。在实际地图中，往往存在着大量这样的斑点，如一颗树是一个斑点，一块草地是一个斑点，一栋房子也可以是一个斑点。由于斑点代表的是一个区域，相比单纯的角点，它的稳定性要好，抗噪声能力要强，所以它在图像配准上扮演了很重要的角色。

同时有时图像中的斑点也是我们关心的区域，比如在医学与生物领域，我们需要从一些X光照片或细胞显微照片中提取一些具有特殊意义的斑点的位置或数量。

比如下图中天空的飞机、向日葵的花盘、X线断层图像中的两个斑点。

"""

# Standard imports
import cv2
import numpy as np

# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
# Detect blobs.
keypoints = detector.detect(im)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
