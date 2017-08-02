# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 10:06
# @Author  : play4fun
# @File    : test1-opencv-python.py
# @Software: PyCharm

"""
test1-opencv-python.py:
"""

import numpy as np
import cv2

print(cv2.__version__, cv2.__doc__)

img = cv2.imread('../../data/messi5.jpg', cv2.IMREAD_UNCHANGED)  # 包括图像的 alpha 通道
rows, cols, ch = img.shape
print('行/高:', rows, '列/宽:', cols, '通道:', ch)

img = cv2.resize(img, (640, 480))

rows, cols, ch = img.shape
print('行/高:', rows, '列/宽:', cols, '通道:', ch)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#
# cv2.imshow('thresh', thresh)  #不支持
# cv2.waitKey(0)
'''
cv2.error: /Users/travis/build/skvark/opencv-python/opencv/modules/highgui/src/window.cpp:583: error: (-2) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Carbon support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function cvShowImage
'''

cv2.imwrite('messi5-gray.jpg', gray)
cv2.imwrite('messi5-thresh.jpg', thresh)
