#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-24 下午5:26
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/contrast75.png',0)
#flatten() 将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])
#计算累积分布图
cdf = hist.cumsum()

##
# 构建 Numpy 掩模数组 cdf 为原数组 当数组元素为 0 时 掩盖(计算时被忽略
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# 对被掩盖的元素赋值，赋值为 0
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
cv2.imshow("img2",img2)
cv2.waitKey(0)

##
#flatten() 将数组变成一维
hist,bins = np.histogram(img2.flatten(),256,[0,256])
#计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()