# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 上午10:57
# @Author  : play4fun
# @File    : 图像相减3.py
# @Software: PyCharm

"""
图像相减3.py:

3张图片

"""
import cv2

def diff(img, img1):  # returns just the difference of the two images
    return cv2.absdiff(img, img1)


def diff_remove_bg(img0, img, img1):  # removes the background but requires three images
    d1 = diff(img0, img)
    d2 = diff(img, img1)
    return cv2.bitwise_and(d1, d2)


# img1=cv2.imread('subtract1.jpg')
img1 = cv2.imread('subtract1.jpg', 0)  # 灰度图
# img2=cv2.imread('subtract2.jpg')
img2 = cv2.imread('subtract2.jpg', 0)

cv2.imshow('subtract1', img1)
cv2.imshow('subtract2', img2)

#
st = diff_remove_bg(img2, img1,img2)

cv2.imshow('after subtract', st)

cv2.waitKey(0)