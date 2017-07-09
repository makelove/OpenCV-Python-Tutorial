# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg', 0)  # gray
print(img.shape)

img = cv2.imread('../data/messi5.jpg')
# print(img.shape)
rows,cols,ch=img.shape
print('行/高:',rows,'列/宽:',cols,'通道:',ch)

print(img.size)
print(img.dtype)
