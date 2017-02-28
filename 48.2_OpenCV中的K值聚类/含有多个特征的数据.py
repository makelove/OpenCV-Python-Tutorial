# -*- coding: utf-8 -*-
# @Time    : 2017/2/24 下午3:14
# @Author  : play4fun
# @File    : 含有多个特征的数据.py
# @Software: PyCharm

"""
含有多个特征的数据.py:
"""

# 在前 的 T 恤例子中我们只考 了   现在我们也把体 考  去 也 就是两个特征。
# 在前一节我们的数据是一个单列向 。每一个特征 排列成一列 每一  对应一个测 样本。
# 在本例中我们的测 数据 应 50x2 的向  其中包含 50 个人的  和 体 。第一列对应与   第二列对应与体 。第一 包含两个元素 第一个 是第一个人的   第二个是第一个人的体 。剩下的 对应与其他人的   和体 。

import numpy as np
import cv2
from matplotlib import pyplot as plt

X = np.random.randint(25, 50, (25, 2))
Y = np.random.randint(60, 85, (25, 2))
Z = np.vstack((X, Y))
# convert to np.float32
Z = np.float32(Z)

# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Now separate the data, Note the flatten()
A = Z[label.ravel() == 0]
B = Z[label.ravel() == 1]

# Plot the data
plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1], c='r')
plt.scatter(center[:, 0], center[:, 1], s=80, c='y', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()
