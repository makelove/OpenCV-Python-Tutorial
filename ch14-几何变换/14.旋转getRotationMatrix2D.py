# -*- coding: utf-8 -*-

# 旋转
import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg', 0)
rows, cols = img.shape

# 的第一个参数为旋转中心 第二个为旋转角度
#  第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)

# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))

cv2.imshow('img', dst)

cv2.waitKey(0)  # & 0xFF
cv2.destroyAllWindows()
