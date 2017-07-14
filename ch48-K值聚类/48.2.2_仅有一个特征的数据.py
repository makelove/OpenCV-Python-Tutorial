# -*- coding: utf-8 -*-
# @Time    : 2017/2/24 下午3:00
# @Author  : play4fun
# @File    : 48.2.2_仅有一个特征的数据.py
# @Software: PyCharm

"""
48.2.2_仅有一个特征的数据.py:

输入参数
1. samples: 应 是 np.float32 类型的数据 每个特征应 放在一列。
2. nclusters(K): 聚类的最终数目。
3. criteria: 终止 代的条件。当条件满 时 算法的 代终止。它应 是 一个含有 3 个成员的元组 它们是 typw max_iter epsilon
4. attempts: 使用不同的 始标 来执 算法的次数。算法会 回紧密度 最好的标 。紧密度也会作为 出  回。
5. flags 用来 置如何 择 始 心。 常我们有两个 择 cv2.KMEANS_PP_CENTERS 和 cv2.KMEANS_RANDOM_CENTERS。

输出参数
1. compactness 紧密度  回每个点到相应 心的 离的平方和。
2. labels 标志数组 与上一节提到的代码相同  每个成员 标 为 0 1 等
3. centers 由聚类的中心组成的数组

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
# 现在我们有一个 度为 50 取值范围为 0 到 255 的向量z。我已经将向量z  重排 将它变成了一个列向量。
# 当每个数据含有多个特征是 会很有用。然后我们数据类型 换成 np.float32。

# exit(0)

##

# 现在我们使用KMeans函数。在之前我们应先置好终止条件。我的终止条件是算法执10次代或者精确度epsilon=1.0。

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# Set flags (Just to avoid line break in the code)

flags = cv2.KMEANS_RANDOM_CENTERS
# Apply KMeans
compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)


# 返回值有紧密度compactness,标志和中心。在本例中我的到的中心是60和207。标志的数目与测数据的多少是相同的每个数据会标上01等。取决与它们的中心是什么。

A = z[labels == 0]
B = z[labels == 1]

# 现在我们可以根据它们的标志将把数据分两组。
# 现在将A组数用红色示
# 将B组数据用蓝色示,重心用黄色示。
# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
plt.hist(A, 256, [0, 256], color='r')
plt.hist(B, 256, [0, 256], color='b')
plt.hist(centers, 32, [0, 256], color='y')
plt.show()
