# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 学习图像上的算术运算 加法 减法 位运算等

# 你可以使用函数 cv2.add() 将两幅图像进行加法运算 当然也可以直接使 用 numpy ，
# res=img1+img
# 两幅图像的大小 类型必须一致 ，或者第二个 图像可以使一个简单的标量值。


x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))  # 250+10 = 260 => 255
# [[255]]
print(x + y)  # 250+10=260%256=4
# [4]


# 图像混合
img1 = cv2.imread('../data/ml.png')
img2 = cv2.imread('../data/opencv_logo.jpg')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # 第一幅图的权重是 0.7 第二幅图的权重是 0.3

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
