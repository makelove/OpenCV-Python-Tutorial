#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-29 上午7:52
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt


filename = '../data/corner-detection.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
#返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()
