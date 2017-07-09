# -*- coding: utf-8 -*-

import numpy as np
import cv2

print(cv2.__version__)

# Load an color image in grayscale
# img = cv2.imread('messi5.jpg', 0)
img = cv2.imread('messi5.jpg')

# img.I
# AttributeError: 'numpy.ndarray' object has no attribute 'I'

#
rows,cols,ch=img.shape
print('行/高:',rows,'列/宽:',cols,'通道:',ch)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)#可以调整窗口大小
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
# cv2.resizeWindow('image', 200, 200)  # 不起作用？

cv2.imshow('image', img)
cv2.waitKey(0)  # 按任意键退出
cv2.destroyAllWindows()

#
# cv2.imwrite('messigray.png', img)
