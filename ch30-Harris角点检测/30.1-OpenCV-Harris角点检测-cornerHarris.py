# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-28 下午7:27

cv2.cornerHarris() 参数如下 
• img - 数据类型为 float32 的 入图像。
• blockSize -  点检测中 考 的 域大小。
• ksize - Sobel 求导中使用的窗口大小
• k - Harris  点检测方程中的自由参数 取值参数为 [0,04 0.06].
"""

import cv2
import numpy as np

filename = '../data/chessboard.png'
# filename = '../data/chessboard-3.png'
# filename = '../data/corner-detection.jpg'

img = cv2.imread(filename)
img = cv2.resize(img, (640, 480))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 输入图像必 是 float32 最后一个参数在 0.04 到 0.05 之间
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
