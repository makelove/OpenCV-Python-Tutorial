# -*- coding: utf-8 -*-
import cv2
import numpy as np

'''
例如我们 检测一副图像中 眼睛的位置 我们 先应该在图像中找到脸 再在脸的区域中找眼睛 
而不是 直接在一幅图像中搜索。这样会提高程序的准确性和性能。
'''

img=cv2.imread('../data/messi5.jpg')

ball=img[280:340,330:390]
img[273:333,100:160]=ball #修改像素值



cv2.namedWindow("messi",0)
cv2.imshow("messi",img)
cv2.waitKey(0)
