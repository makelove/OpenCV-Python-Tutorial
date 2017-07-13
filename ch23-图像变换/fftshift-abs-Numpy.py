# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-24 下午5:42

现在我们可以   域变换了 我们就可以在 域对图像  一些操 作了 例如  滤波和 建图像 DFT 的 变换 。比如我们可以使用一个 60x60 的矩形窗口对图像  掩模操作从而去 低 分 。然后再使用函数 np.fft.ifftshift()    平移操作 所以现在直流分 又回到左上 了 左 后使用函数 np.ifft2()    FFT  变换。同样又得到一堆复杂的数字 我们 可以对他们取绝对值 

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()

'''
如果你 察仔细的  尤其是最后一章 JET  色的图像 你会看到一些不 自然的东  如我用红色箭头标出的区域 。看上图  有些条带 的结构    成为振铃效应。
 这是由于我们使用矩形窗口做掩模 成的。 个掩模  换 成正弦形状时就会出现 个  。所以一般我们不 用矩形窗口滤波。最好的  择是高斯窗口。

'''
