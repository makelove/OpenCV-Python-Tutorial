# -*- coding: utf-8 -*-


import cv2
import numpy as np
img=cv2.imread('../data/messi5.jpg')
# 下mian的 None 本应 是 出图像的尺寸 但是因为后 我们 置了缩放因子
# 因此  为 None
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#OR
#   呢 我们直接 置 出图像的尺寸 所以不用 置缩放因子
height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()