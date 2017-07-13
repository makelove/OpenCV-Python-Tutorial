# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午6:18
# @Author  : play4fun
# @File    : 41.4-BackgroundSubtractorGMG.py
# @Software: PyCharm

"""
41.4-BackgroundSubtractorGMG.py:

它使用前 很少的图像   为前 120 帧   背景建模。使用了概率前 景估 算法 使用 叶斯估  定前景 。 是一种自 应的估  新 察到的 对 比旧的对 具有更 的权  从而对光照变化产生 应。一些形态学操作 如开 算  算等 用来 去不  的噪 。在前几帧图像中你会得到一个  色窗口。
  对结果  形态学开 算对与去 噪声很有帮助。
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorGMG()
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
