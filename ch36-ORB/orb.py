# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午3:45
# @Author  : play4fun
# @File    : orb.py
# @Software: PyCharm

"""
orb.py:
SIFT 和 SURF 算法是有专利保护的 如果你 使用它们 就可能要花钱 。但是 ORB 不需要

ORB 基本是 FAST 关 点检测和 BRIEF 关 点描 器的结合体 并
 很多修改增强了性能。 先它使用 FAST 找到关 点 然后再使用 Harris  点检测对 些关 点  排序找到其中的前 N 个点。它也使用 字塔从而产 生尺度不变性特征。

 数据的方差大的一个好处是 使得特征更容易分辨。

对于描述符，ORB使用BRIEF描述符。但我们已经看到，这个BRIEF的表现在旋转方面表现不佳。因此，ORB所做的是根据关键点的方向来“引导”。
对于在位置(xi，yi)的n个二进制测试的任何特性集，定义一个包含这些像素坐标的2 n矩阵。然后利用补丁的方向，找到旋转矩阵并旋转S，以得到引导(旋转)版本s。

ORB将角度进行离散化，以增加2/30(12度)，并构造一个预先计算过的简短模式的查找表。只要键点的方向是一致的，就会使用正确的点集来计算它的描述符。

BRIEF有一个重要的属性，即每个比特的特性都有很大的方差，而平均值接近0.5。但是一旦它沿着键点方向移动，它就会失去这个属性并变得更加分散。高方差使特征更有区别，因为它对输入的响应不同。另一个可取的特性是让测试不相关，因为每个测试都将对结果有所贡献。为了解决所有这些问题，ORB在所有可能的二进制测试中运行一个贪婪的搜索，以找到那些既有高方差又接近0.5的，同时又不相关的。结果被称为rBRIEF。

对于描述符匹配，在传统的LSH上改进的多探测LSH是被使用的。这篇文章说，ORB比冲浪快得多，而且比冲浪还好。对于全景拼接的低功率设备，ORB是一个不错的选择。

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/blox.jpg', 0)

# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img, None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)

plt.imshow(img2), plt.show()
