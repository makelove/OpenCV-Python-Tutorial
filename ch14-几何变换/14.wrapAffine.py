# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 移动了100,50 个像素。
img = cv2.imread('../data/messi5.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
