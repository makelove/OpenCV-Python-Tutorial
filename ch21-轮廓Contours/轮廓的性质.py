# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午8:38
# @Author  : play4fun
# @File    : 轮廓的性质.py
# @Software: PyCharm

"""
轮廓的性质.py:
"""
import cv2
import numpy as np

# 边界矩形的宽高比
x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w) / h

# Extent轮廓面积与边界矩形面积的比。
area = cv2.contourArea(cnt)
x, y, w, h = cv2.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area

# Solidity轮廓面积与凸包面积的比。
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area) / hull_area

# Equivalent Diameter与轮廓面积相等的圆形的直径
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)

# Orientation对象的方向 下 的方法 会返回  长轴和短轴的长度
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)

# Mask and Pixel Points掩模和像素点
mask = np.zeros(imgray.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv2.findNonZero(mask)
# 第一种方法使用了 Numpy 函数
# 第二种使用 了 OpenCV 函数。
# 结果相同 但还是有点不同。Numpy 给出的坐标是 (row ,colum)
# 而 OpenCV 给出的格式是 (x y )形式的。所以 两个结果基 本是可以互换的。row=x ,colunm=y。

# 最大值和最小值及它们的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray, mask=mask)

# 平均 色及平均灰度 我们也可以使用相同的掩模求一个对 的平均 色或平均灰度
mean_val = cv2.mean(im, mask=mask)

# 极点 一个对象最上面  最下面  最左  最右 的点。
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
