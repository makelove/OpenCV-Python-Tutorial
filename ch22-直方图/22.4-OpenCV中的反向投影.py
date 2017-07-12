# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午11:06
# @Author  : play4fun
# @File    : 22.4-OpenCV中的反向投影.py
# @Software: PyCharm

"""
22.4-OpenCV中的反向投影.py:
OpenCV 提供的函数 cv2.calcBackProject() 可以用来做直方图反向 投影。
它的参数与函数 cv2.calcHist 的参数基本相同。
其中的一个参数是我 们 查找目标的直方图。
同样再使用目标的直方图做反向投影之前
我们应 先 对其做归一化处理。
 返回的结果是一个概率图像 我们再使用一个圆盘形卷积 核对其做卷操作 最后使用 值  二值化
"""

import cv2
import numpy as np

roi = cv2.imread('tar.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
target = cv2.imread('roi.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
# calculating object histogram
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# normalize histogram and apply backprojection
# 归一化 原始图像 结果图像 映射到结果图像中的最小值 最大值 归一化类型
# cv2.NORM_MINMAX 对数组的所有值进行转化 使它们线性映射到最小值和最大值之  间
#  归一化之后的直方图便于显示 归一化之后就成了 0 到 255 之 的数了。
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# Now convolute with circular disc
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)
# threshold and binary AND
ret, thresh = cv2.threshold(dst, 50, 255, 0)

# 别忘了是三  图像 因此  使用 merge 变成 3
thresh = cv2.merge((thresh, thresh, thresh))

# 按位操作
res = cv2.bitwise_and(target, thresh)
res = np.hstack((target, thresh, res))
cv2.imwrite('res.jpg', res)

# 显示图像
cv2.imshow('1', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
