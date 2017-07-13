# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 上午10:59
# @Author  : play4fun
# @File    : OpenCV中的傅里叶变换-DFT.py
# @Software: PyCharm

"""
OpenCV中的傅里叶变换-DFT.py:
OpenCV 中相应的函数是 cv2.dft() 和 cv2.idft()。和前  出的结果 一样 但是是双通道的。
第一个通道是结果的实数部 分
第二个通道是结果的虚数部分。
输入图像  先 换成 np.float32 格式

使用函数 cv2.cartToPolar() 它会同时返回幅度和相位。

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg', 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
