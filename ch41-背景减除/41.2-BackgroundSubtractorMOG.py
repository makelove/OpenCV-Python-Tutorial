# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午6:12
# @Author  : play4fun
# @File    : 41.2-BackgroundSubtractorMOG.py
# @Software: PyCharm

"""
41.2-BackgroundSubtractorMOG.py:
在很多基础应用中背景检出 是一个 常  的步 。例如 客统  使 用一个 态摄像头来 录 入和离开房 的人数 或者是交 摄像头   提 取交 工具的信息等。在所有的 些例子中  先 将人或 单独提取出来。 技术上来  我们  从 止的背景中提取移动的前景。

但是我们现在讲的背景建模是基于时间序列的
 因此每一个像素点所在的位置在整个时间序列中 就会有很多值 从而构成一个分布。
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG()
# 可选参数 比如 进行建模场景的时间长度 高斯混合成分的数量-阈值等

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
