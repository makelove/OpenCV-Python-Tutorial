# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午7:49
# @Author  : play4fun
# @File    : 21.1.2 怎样绘制轮轮廓.py
# @Software: PyCharm

"""
21.1.2 怎样绘制轮轮廓.py:
函数 cv2.drawContours() 可以 用来绘制 轮廓。它可以根据你提供 的 界点绘制任何形状。
第一个参数是原始图像 
第二个参数是 轮廓 一 个 Python 列表。
第三个参数是 轮廓的索引
在绘制独立 轮廓是很有用 当 设置为 -1 时绘制所有轮廓 。
接下来的参数是 轮廓的颜色和厚度等。
"""

import numpy as np
import cv2

im = cv2.imread('../data/cards.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray', imgray)

ret, thresh = cv2.threshold(imgray, 244, 255, 0)

img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('len(contours', len(contours))

# cv2.drawContours(imgray, contours, -1, (0, 0,255), 3)
cv2.drawContours(im, contours, -1, (255, 0, 0), 3)

if len(contours) > 4:
    # To gdraw an individual contour, say 4th contour:
    # 绘制独立 轮廓 如第四个 轮廓
    cv2.drawContours(image=im, contours=contours, contourIdx=3, color=(0, 0, 255), thickness=3)
    # drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None)

    # But most of the time, below method will be useful:
    # 但是大多数时候 下 的方法更有用
    cnt = contours[4]
    cv2.drawContours(im, [cnt], 0, (0, 255, 0), 3)

# 第一个contour
print('contours[0]:', contours[0])
cv2.drawContours(imgray, contours[0], 0, (0, 0, 255), 3)

'''
 这个参数如果 设置为 cv2.CHAIN_APPROX_NONE 
 所有的边界点 都 会被存储。但是我们真的需要那么多点吗 ？
 例如 当我们找的边界是一条直线时。你需要直线上所有的点来表示直线吗 ？
 不是的 我们只需要1 条直线 的两个端点而已。 
 就是 cv2.CHAIN_APPROX_SIMPLE  做的。它会
将 轮廓上的冗余点 去掉， 压缩 轮廓 ，从而节省内存开支。
'''

cv2.imshow('drawContours', im)
cv2.imshow('drawContours-imgray', imgray)
cv2.waitKey(0)
