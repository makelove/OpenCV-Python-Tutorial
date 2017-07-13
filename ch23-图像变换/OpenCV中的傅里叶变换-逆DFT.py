# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 上午11:03
# @Author  : play4fun
# @File    : OpenCV中的傅里叶变换-逆DFT.py
# @Software: PyCharm

"""
OpenCV中的傅里叶变换-逆DFT.py:
在前 的 分我们实现了一个 HPF 高通滤波   现在我们来做 LPF 低通滤波 将高频分去除。其实就是对图像进行模糊操作。
 首先我们  构建一个掩模 与低 区域对应的地方 置为 1, 与  区域 对应的地方 置为 0。
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg', 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

# apply mask and inverse DFT
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
