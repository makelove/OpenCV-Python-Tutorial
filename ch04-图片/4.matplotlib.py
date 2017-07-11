import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
# 彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotlib 是 RGB 模式。所以彩色图像如果已经被OpenCV 读取，  它将不会被 Matplotlib 正 确显示。

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
