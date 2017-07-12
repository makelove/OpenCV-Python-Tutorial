# -*- coding: utf-8 -*-
'''
与腐 相反 与卷积核对应的原图像的像素值中只 有一个是 1 中心元 素的像素值就是 1。所以 个操作会增加图像中的白色区域 前景 。一般在去 噪声时先用腐 再用膨胀。因为腐 在去掉白噪声的同时 也会使前景对 变 小。所以我们再对他  膨胀。 时噪声已经 去 了 不会再回来了 但是 前景 在并会增加。膨胀也可以用来 接两个分开的物体。
'''

import cv2
import numpy as np

img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('dilation', dilation)
cv2.moveWindow('dilation', x=img.shape[1], y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()
