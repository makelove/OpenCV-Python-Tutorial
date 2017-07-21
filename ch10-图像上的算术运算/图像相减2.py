# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 上午10:48
# @Author  : play4fun
# @File    : 图像相减2.py
# @Software: PyCharm

"""
图像相减2.py:
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img1=cv2.imread('subtract1.jpg')
img1 = cv2.imread('subtract1.jpg', 0)  # 灰度图
# img2=cv2.imread('subtract2.jpg')
# img2 = cv2.imread('subtract2.jpg', 0)
img22 = cv2.imread('subtract2.jpg')
img2=cv2.cvtColor(img22,cv2.COLOR_BGR2GRAY)

cv2.imshow('subtract1', img1)
cv2.imshow('subtract2', img2)

#
st = cv2.subtract(img2, img1)
# st = cv2.subtract(img1, img2)#相反
st[st<=5]=0 #把小于20的像素点设为0

cv2.imshow('after subtract', st)


'''
# 直方图，看看大部分像素集中在哪个区域
# plt.plot(st)
pxs = st.ravel()
pxs=[x for x in pxs if x>5]#20,10
plt.hist(pxs, 256, [0, 256])
plt.show()
'''

# 效果好一点
# ret,threshold=cv2.threshold(st,0, 127, cv2.THRESH_BINARY)
ret, threshold = cv2.threshold(st, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('after threshold', threshold)

#TODO 截取原图，把长方形纠正
image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


areas=list()
for i,cnt in enumerate(contours):
    areas.append((i,cv2.contourArea(cnt)))

#
a2=sorted(areas,key=lambda d:d[1],reverse=True)

for i,are in a2:
    if are <100:
        continue
    cv2.drawContours(img22, contours, i, (0, 0, 255), 3)
    print(i,are)

    cv2.imshow('drawContours',img22)
    cv2.waitKey(0)

cv2.destroyAllWindows()
