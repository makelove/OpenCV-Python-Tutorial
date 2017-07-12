# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午1:27
# @Author  : play4fun
# @File    : 15-How-OTSU-work.py
# @Software: PyCharm

"""
15-How-OTSU-work.py:
"""

import cv2
import numpy as np

img = cv2.imread('noisy2.png', 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
# find normalized_histogram, and its cumulative distribution function
#  算归一化直方图
# CalcHist(image, accumulate=0, mask=NULL)

hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.max()
Q = hist_norm.cumsum()

bins = np.arange(256)
fn_min = np.inf
thresh = -1

for i in range(1, 256):
    p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
    q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
    b1, b2 = np.hsplit(bins, [i])  # weights

    # finding means and variances
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

    # calculates the minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(thresh, ret)
