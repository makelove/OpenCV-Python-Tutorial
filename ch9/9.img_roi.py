# -*- coding: utf-8 -*-
import cv2
import numpy as np

img=cv2.imread('../data/messi5.jpg')

ball=img[280:340,330:390]
img[273:333,100:160]=ball



cv2.namedWindow("messi",0)
cv2.imshow("messi",img)
cv2.waitKey(0)
