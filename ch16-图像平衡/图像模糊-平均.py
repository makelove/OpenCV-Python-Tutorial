# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午1:35
# @Author  : play4fun
# @File    : 图像模糊-平均.py
# @Software: PyCharm

"""
图像模糊-平均.py:
 是由一个归一化卷积框完成的。他只是用卷积框 盖区域所有像素的平 均值来代替中心元素。可以使用函数 cv2.blur() 和 cv2.boxFilter() 来完  个任务。
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/opencv_logo.png')
# blur = cv2.blur(img, (5, 5))

'''
现在把卷积核换成 斯核 简单来  方框不变 将原来每个方框的值是 相等的 现在  的值是符合 斯分布的 方框中心的值最大 其余方框根据  离中心元素的 离 减 构成一个 斯小山包。原来的求平均数现在变成求 加权平均数 全就是方框 的值 。
'''
# 0 是指根据窗口大小 5,5 来计算高斯函数标准差
blur = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯模糊

'''
 名思义就是用与卷积框对应像素的中值来替代中心像素的值。 个滤波 器经常用来去 椒盐噪声。前 的滤波器 是用 算得到的一个新值来取代中 心像素的值 而中值滤波是用中心像素周围 也可以使他本  的值来取代他。 他能有效的去 噪声。卷积核的大小也应 是一个奇数。
'''
median = cv2.medianBlur(img, 5)  # 中值模糊

'''
函数 cv2.bilateralFilter() 能在保持边界清晰的情况下有效的去 噪  。
但是 种操作与其他滤波器相比会比 慢。
我们已经知 高斯滤波器是求 中心点 邻近区域像素的高斯加权平均值。
 种 斯滤波器只考虑像素之间的空间关系 
 而不会考虑像素值之间的关系 ，像素的相似度 。
 所以 种方法不会考 虑 一个像素是否位于边界。
 因此边界也会被模糊掉 而 这正不是我们想要。

双边滤波在同时使用空 高斯权重和灰度值相似性 斯权 。
空 高斯函数确保只有邻近区域的像素对中心点有影响
 灰度值相似性高斯函数确保只有与中心像素灰度值相近的才会被用来做模糊运算。
 所以 种方法会确保边界不会被模糊掉
  因为边界处的灰度值变化比较大。
'''

# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# d – Diameter of each pixel neighborhood that is used during filtering. # If it is non-positive, it is computed from sigmaSpace
# 9  域直径 两个 75 分别是空  斯函数标准差 灰度值相似性 斯函数标准差
blur = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
