# -*- coding: utf-8 -*-

'''
图像 字塔的一个应用是图像 合。例如 在图像缝合中 你  将两幅 图叠在一  但是由于 接区域图像像素的不 续性 整幅图的效果看 来会 很差。 时图像 字塔就可以排上用场了 他可以帮你实现无缝 接。  的 一个经典案例就是将两个水果 合成一个 看看下图也 你就明白我在 什么 了。


实现上 效果的步 如下
1.  入两幅图像 苹果和句子
2. 构建苹果和橘子的 斯 字塔 6 层
3. 根据 斯 字塔 算拉普拉斯 字塔
4. 在拉普拉斯的每一层  图像 合 苹果的左 与橘子的右  合  5. 根据 合后的图像 字塔 建原始图像。
'''

import cv2
import numpy as np, sys

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i - 1], GE)#TODO error
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
# numpy.hstack(tup)
# Take a sequence of arrays and stack them horizontally
# to make a single array.
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))

cv2.imwrite('Pyramid_blending2.jpg', ls_)
cv2.imwrite('Direct_blending.jpg', real)
