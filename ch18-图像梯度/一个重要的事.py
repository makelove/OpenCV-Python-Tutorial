# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午2:23
# @Author  : play4fun
# @File    : 一个重要的事.py
# @Software: PyCharm

"""
一个重要的事.py:
当我们可以  参 数 -1 来 定 出图像的深度 数据类型 与原图像保持一致
但是我们在代 码中使用的却是 cv2.CV_64F。 是为什么呢 ？
想象一下一个从黑到白的边界的导数是整数，而一个从白到黑的边界点导数却是负数。
如果原图像的深度是 np.int8 时 所有的负值 会 截断变成 0
 换句话就是把边界丢失掉。
所以如果 两种边界你 想检测到
最好的的办法就是将输出的数据类型 设置的更高
  比如 cv2.CV_16S cv2.CV_64F 等。
  取绝对值然后再把它 回 到 cv2.CV_8U。
  下 的示例演示了输出图片的深度不同造成的不同效果。
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/box.png', 0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()
