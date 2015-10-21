# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread('../data/messi5.jpg',0)
rows,cols=img.shape
#的第一个参数为旋 中心 第二个为旋  度 第三个为旋 后的缩放因子
# 可以    置旋 中心 缩放因子 以及窗口大小来 止旋 后 出 界的
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
# 第三个参数是 出图像的尺寸中心
dst=cv2.warpAffine(img,M,(2*cols,2*rows))
while(1):
    cv2.imshow('img',dst)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.destroyAllWindows()