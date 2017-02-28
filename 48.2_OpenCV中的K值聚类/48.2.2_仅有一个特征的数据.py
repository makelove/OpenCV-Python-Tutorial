# -*- coding: utf-8 -*-
# @Time    : 2017/2/24 下午3:00
# @Author  : play4fun
# @File    : 48.2.2_仅有一个特征的数据.py
# @Software: PyCharm

"""
48.2.2_仅有一个特征的数据.py:
"""

# 假 我们有一组数据 每个数据只有一个特征 1 维 。例如前 的 T 恤    我们只使用人们的  来决定 T 恤的大小。
# 我们先来产生一些 机数据 并使用 Matplotlib 将它们绘制出来。

import numpy as np
import cv2
from matplotlib import pyplot as plt

x = np.random.randint(25, 100, 25)
y = np.random.randint(175, 255, 25)
z = np.hstack((x, y))
z = z.reshape((50, 1))
z = np.float32(z)
plt.hist(z, 256, [0, 256]), plt.show()
# 现在我们有一个 度为 50 取值范围为 0 到 255 的向  z。我已经将向   z   了 排 将它变成了一个列向 。当每个数据含有多个特征是 会很 有用。然后我们数据类型 换成 np.float32。

##

# 现在我们使用KMeans函数。在之前我们应先置好终止条件。我的终止条件是算法执10次代或者精确度epsilon=1.0。

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# Set flags (Just to avoid line break in the code)

flags = cv2.KMEANS_RANDOM_CENTERS
# Apply KMeans
compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)
# 返回值有紧密度compactness,标志和中心。在本例中我的到的中心是60和207。标志的数目与测数据的多少是相同的每个数据会标上01等。取决与它们的中心是什么。现在我们可以根据它们的标志将把数据分两组。现在将A组数用红色示将B组数据用蓝色示心用色示。
A = z[labels == 0]
B = z[labels == 1]
# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
plt.hist(A, 256, [0, 256], color='r')
plt.hist(B, 256, [0, 256], color='b')
plt.hist(centers, 32, [0, 256], color='y')
plt.show()
