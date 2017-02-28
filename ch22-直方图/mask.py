#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-24 下午5:22
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('../data/home.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),
plt.subplot(222),
plt.subplot(223),
plt.subplot(224),
plt.xlim([0,256])
plt.imshow(img, 'gray')
plt.imshow(mask,'gray')
plt.imshow(masked_img, 'gray')
plt.plot(hist_full), plt.plot(hist_mask)
plt.show()