# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg', 0)  # gray
print(img.shape)

img = cv2.imread('../data/messi5.jpg')
print(img.shape)

print(img.size)
print(img.dtype)
