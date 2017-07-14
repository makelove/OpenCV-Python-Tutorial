# -*- coding: utf-8 -*-
'''
透视变换
对于透视变换 ，我们需要一个 3x3 变换矩 。
在变换前后直线 是直线。
构建 个变换矩  你需要在输入图像上找 4 个点， 以及他们在输出图 像上对应的位置。
四个点中的任意三个都不能共线。这个变换矩阵可以用函数 cv2.getPerspectiveTransform() 构建。
然后把这个矩阵传给函数 cv2.warpPerspective。

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/sudoku.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

plt.figure(figsize=(8, 7), dpi=98)
p1 = plt.subplot(211)
p1.imshow(img)
p1.set_title('Input')

p2 = plt.subplot(212)
p2.imshow(dst)
p2.set_title('Output')

plt.show()
