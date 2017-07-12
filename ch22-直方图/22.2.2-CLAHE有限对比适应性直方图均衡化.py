# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午10:18
# @Author  : play4fun
# @File    : 22.2.2-CLAHE有限对比适应性直方图均衡化.py
# @Software: PyCharm

"""
22.2.2-CLAHE有限对比适应性直方图均衡化.py:

自 应的直方图均 化。 种情况下  整幅图像会 分成很多小块  些小块 称为 tiles
在 OpenCV 中 tiles 的 大小  是 8x8
然后再对每一个小块分别  直方图均 化  前 类似 。 所以在每一个的区域中 直方图会 中在某一个小的区域中   有噪声干 扰 。

如果有噪声的  噪声会 放大。为了 免 种情况的出现 使用对比度  制。对于每个小块来  如果直方图中的 bin   对比度的上 的  就把 其中的像素点均匀分散到其他 bins 中 然后在  直方图均 化。

最后 为了 去 每一个小块之  人 的 由于算法 成  界 再使用双线性差值 对 小块  缝合。

"""

import numpy as np
import cv2

img = cv2.imread('tsukuba_l.png', 0)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg', cl1)
