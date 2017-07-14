# -*- coding: utf-8 -*-
# @Time    : 2017/2/24 下午3:17
# @Author  : play4fun
# @File    : 48.2.3_颜色量化.py
# @Software: PyCharm

"""
48.2.3_颜色量化.py:
"""

# 颜色量化就是减少图片中颜色数目的一个过程。为什么 减少图片中的  色呢 减少内存消耗 有些 备的 源有  只能显示很少的 色。在 种情 况下就     色 化。我们使用 K 值聚类的方法来   色 化。
# 没有什么新的知   介绍了。现在有 3 个特征 R G B。所以我们   把图片数据变形成 Mx3 M 是图片中像素点的数目 的向 。聚类完成后  我们用聚类中心值替换与其同组的像素值  样结果图片就只含有指定数目的  色了。下 是代码
# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('../data/home.jpg')
# img = cv2.imread('../data/opencv_logo.png')
Z = img.reshape((-1, 3))
# convert to np.float32
Z = np.float32(Z)


# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# K = 8
# K = 3
K = 14
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)


# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
