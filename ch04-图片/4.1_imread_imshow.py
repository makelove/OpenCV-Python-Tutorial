# -*- coding: utf-8 -*-

import numpy as np
import cv2

print(cv2.__version__)


# img = cv2.imread('messi5.jpg',cv2.IMREAD_COLOR)#读入一副彩色图像。图像的透明度会被忽略   默认参数。
# img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)# Load an color image in grayscale 灰度
img = cv2.imread('messi5.jpg',cv2.IMREAD_UNCHANGED)#包括图像的 alpha 通道

# img.I
# AttributeError: 'numpy.ndarray' object has no attribute 'I'

#
rows,cols,ch=img.shape
print('行/高:',rows,'列/宽:',cols,'通道:',ch)
#图像的宽对应的是列数, 高对应的是行数。

cv2.namedWindow('image', cv2.WINDOW_NORMAL)#可以调整窗口大小
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)#自动调整
# cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)#保持图片比例

# cv2.resizeWindow('image', 200, 200)  # 不起作用？

cv2.imshow('image', img)#窗口会自动调整为图像大小
# 按任意键退出
cv2.waitKey(0)#返回按键的 ASCII 码值

cv2.destroyAllWindows()

#
# cv2.imwrite('messigray.png', img)
