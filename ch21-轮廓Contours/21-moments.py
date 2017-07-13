# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-23 下午12:56
图像的矩可以帮助我们计算图像的质心， 面积等。
"""

import cv2
import numpy as np

from pprint import pprint

img = cv2.imread('../data/star.png', 0)
# img = cv2.imread('../data/box.png', 0)

ret, thresh = cv2.threshold(img, 127, 255, 0)
# ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(thresh, 1, 2)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print('contours len:', len(contours))

cnt = contours[0]  # 第一个
M = cv2.moments(cnt)

# print(M)
pprint(M)  # 好看一点

# 根据 这些矩的值 我们可以 计算出对象的重心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print('重心:', cx, cy)

#
area = cv2.contourArea(cnt)
print('面积:', area)

# 第二参数可以用来指定对象的形状是闭合的 True   是打开的FALSE 一条曲线 。
perimeter = cv2.arcLength(cnt, True)
print('周长:', perimeter)

'''
将轮廓形状近似到另外一种由更少点组成的 廓形状 新 廓的点的数目 由我们 定的准确度来决定。
使用的Douglas-Peucker算法 
为了帮助理解，假设我们 在一幅图像中查找一个矩形 
但是由于图像的 种种原因，我们不能得到一个完美的矩形 而是一个 坏形状 如下图所示 。 

现在你就可以使用这个函数来近似 个形状  了。
 这个函数的第二个参数叫 epsilon 它是从原始 廓到近似轮廓的最大距离。它是一个准确度参数。  
 选择一个好的 epsilon 对于得到满意结果非常重要
'''
epsilon = 0.1*cv2.arcLength(cnt,True)
print('epsilon:',epsilon)
approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(image,[approx],0,(255,0,0),3)
cv2.imshow('approxPolyDP',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
