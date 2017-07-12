# -*- coding: utf-8 -*-

'''
2D 卷积
OpenCV 提供的函数 cv.filter2D() 可以 我们对一幅图像  卷积操
作。
操作如下 将核放在图像的一个像素 A 上 求与核对应的图像上 25 5x5  个像素的和 在取平均数 用 个平均数替代像素 A 的值。 复以上操作直到 将图像的每一个像素值 更新一 。
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/opencv_logo.png')
kernel = np.ones((5, 5), np.float32) / 25
# cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
# ddepth –desired depth of the destination image;
# if it is negative, it will be the same as src.depth();
# the following combinations of src.depth() and ddepth are supported:
# src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
# src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
# src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
# src.depth() = CV_64F, ddepth = -1/CV_64F
# when ddepth=-1, the output image will have the same depth as the source.

dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.show()
