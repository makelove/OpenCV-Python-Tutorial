# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 按位运算

# Load two images
img1 = cv2.imread('../data/messi5.jpg')
img2 = cv2.imread('../data/opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # opencv 3.0
#TODO error

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 左 的图像是我们创建的掩码。右 的是最终结果。
# 为了帮助大 家理解，我把上面程序的中间结果也显示了出来
# 特别是 img1_bg 和 img2_fg。
