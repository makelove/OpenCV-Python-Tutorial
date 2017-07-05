# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg')
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
