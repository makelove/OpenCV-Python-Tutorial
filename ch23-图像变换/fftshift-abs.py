#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-24 下午5:42
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


rows, cols = img.shape
crow,ccol = rows/2 , cols/2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()