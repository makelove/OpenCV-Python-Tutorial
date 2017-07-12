# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午3:06
# @Author  : play4fun
# @File    : 图像金字塔.py
# @Software: PyCharm

"""
图像金字塔.py:
一般情况下 我们 处理是一副具有固定分辨率的图像。
但是有些情况下  我们  对同一图像的不同分 率的子图像  处理。
比如 我们 在一幅图 像中查找某个目标 比如脸 我们不知 目标在图像中的尺寸大小。
 这种情况下 ，我们  创建创建一组图像 ， 这些图像是具有不同分 率的原始图像。
 我们把这组图像叫做图像金字塔
 简单来说 就是同一图像的不同分辨率的子图集合 。

 如果我们把最大的图像放在底部，最小的放在顶部
看起来像一座金字塔， 故而得名：图像金字塔。
  有两类图像金字塔： 高斯金字塔和拉普拉斯金字塔。

高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的。
图像中的每个像素值等于下一层图像中 5 个像素的 斯加权平均值。
这样 操作一次一个 MxN 的图像就变成了一个 M/2xN/2 的图像。
所以 这幅图像 的面积就变为原来图像面积的四分之一。 这称为 Octave。
连续进行这样 的操作我们就会得到一个分辨率不断下降的图像金字塔。
我们可以使用函数 cv2.pyrDown() 和 cv2.pyrUp() 构建图像金字塔。


"""

import cv2
import numpy as np

higher_reso = cv2.imread('../data/messi5.jpg')
# 函数 cv2.pyrDown() 从一个 分辨率大尺寸的图像向上构建一个金子塔
# 尺寸变小 分辨率降低 。
lower_reso = cv2.pyrDown(higher_reso)
cv2.imshow('lower_reso', lower_reso)

# 从一个低分 率小尺寸的图像向下构建一个 子塔 尺 寸变大 但分 率不会增加
higher_reso2 = cv2.pyrUp(lower_reso)
cv2.imshow('higher_reso2', higher_reso2)

# 你  住的是是 higher_reso2 和 higher_reso 是不同的。因为一旦使 用 cv2.pyrDown() 图像的分辨率就会 低 ,信息就会 丢失

cv2.waitKey(0)
cv2.destroyAllWindows()
