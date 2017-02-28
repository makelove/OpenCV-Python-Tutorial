#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-25 下午12:09
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('../data/water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
#距离变换的基本含义是计算一个图像中非像素点到最近的零像素点的距离
# 也就是到零像素点的最短距离
# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现,
# 腐蚀操作的停止条件是所有前景像素都被完全腐蚀。
# 这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心骨架像素点的距离
# 根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
#cv2.distanceTransform(src, distanceType, maskSize)
# 第二个参数 0,1,2 分别 示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
dist_transform = cv2.distanceTransform(opening,1,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)