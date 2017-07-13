# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午6:16
# @Author  : play4fun
# @File    : 41.3-BackgroundSubtractorMOG2.py
# @Software: PyCharm

"""
41.3-BackgroundSubtractorMOG2.py:
这个算法的一个特点是它为每一个像素选择一个合适数目的 斯分布。
上一个方法中我们使用是 K 给斯分 布 。
 这样就会对由于亮度等发生变化引起的场景变化产生更好的适应。
和前面一样我们  创建一个背景对 。但在  我们我们可以 择是否 检测阴影。如果 detectShadows = True 默认值
它就会检测并将影子标记出来 但是 样做会降低处理速度。影子会 标记为灰色。
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
