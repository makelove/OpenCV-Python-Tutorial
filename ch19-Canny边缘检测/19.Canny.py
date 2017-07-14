# -*- coding: utf-8 -*-

'''
Canny 边缘检测是一种 常流 的 缘检测算法 是 John F.Canny 在
1986 年提出的。它是一个有很多步构成的算法
由于 缘检测很容易受到噪声影响 所以第一步是使用 5x5 的 斯滤波器 去 噪声
对平滑后的图像使用 Sobel 算子 算水平方向和竖直方向的一 导数 图 像梯度  Gx 和 Gy
梯度的方向一般总是与边界垂直。
梯度方向 归为四类： 垂直 水平 和 两个对角线。
非极大值抑制

滞后阈值
现在 确定 些 界才是真正的边界。 时我们   置两个阈值  minVal 和 maxVal。
当图像的灰度梯度 于 maxVal 时  为是真的边界
那些低于 minVal 的 界会 抛弃。
如果介于两者之间的  就 看这个点是否与某个被确定为真正的边界点相连
如果是就认为它也是边界点 如果不是 就抛弃。

OpenCV 中的 Canny 边界检测
在 OpenCV 中只 需要 一个函数 cv2.Canny() 就可以完成以上几步。
  我们看如何使用这个函数。
第一个参数是输入图像。
第二和第三 个分别是 minVal 和 maxVal。
第三个参数 置用来计算图像梯度的 Sobel卷积核的大小  默认值为 3。
最后一个参数是 L2gradient 它可以用来 设定 求梯度大小的方程。
如果 为 True 就会使用我们上 提到 的方程 否则 使用方程 Edge−Gradient (G) = |G2x| + |G2y| 代替，  默认值为 False。
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg',0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
