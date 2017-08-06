# -*- coding: utf-8 -*-
'''
两个基本的形态学操作是腐 和膨胀。他们 的变体构成了开运算 ，闭运算， 梯度等。

根据卷积核的大小  前景的所有像素 会 腐  掉 变为 0  ，所以前景物体会变小 整幅图像的白色区域会减少。
对于去除白噪声很有用 也可以用来断开两个 在一块的物体等。
'''

import cv2
import numpy as np

img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)

#您可以将内核看作是一个小矩阵，我们在图像上滑动以进行（卷积）操作，例如模糊，锐化，边缘检测或其他图像处理操作。
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('erode', erosion)
cv2.moveWindow('erode', x=img.shape[1], y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()
