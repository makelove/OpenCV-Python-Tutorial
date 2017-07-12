# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午9:25
# @Author  : play4fun
# @File    : 凸缺陷.py
# @Software: PyCharm

"""
凸缺陷.py:
"""

# 凸缺陷
# 前 我们已经学习了 廓的凸包 对 上的任何凹   成为凸缺 。
# OpenCV 中有一个函数 cv.convexityDefect() 可以帮助我们找到凸缺


# hull = cv2.convexHull(cnt, returnPoints=False)
# defects = cv2.convexityDefects(cnt, hull)


# 注意 如果 查找凸缺  在使用函数 cv2.convexHull 找凸包时 参数 returnPoints 一定 是 False
'''
它会 回一个数组 其中每一 包含的值是 [ 点 终点 最 的点 到最  点的 似 离]。我们可以在一张图上显示它。我们将 点和终点用一条绿线  接 在最 点画一个圆圈   住的是 回结果的前三个值是 廓点的索引。 所以我们  到 廓点中去找它们。
'''
import cv2
import numpy as np

img = cv2.imread('star.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 2, 1)

cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
