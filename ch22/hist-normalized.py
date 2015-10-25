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
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()