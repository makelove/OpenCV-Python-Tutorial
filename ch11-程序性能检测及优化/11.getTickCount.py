# -*- coding: utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread('../data/ml.jpg')

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print (t)
# Result I got is 0.521107655 seconds