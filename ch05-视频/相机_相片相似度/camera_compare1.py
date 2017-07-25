# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 23:39
# @Author  : play4fun
# @File    : camera_compare1.py
# @Software: PyCharm

"""
camera_compare1.py:
"""

from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from utils import mse

cap = cv2.VideoCapture(0)

# frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 4 ，720
# frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 3   ，1280
# frame_height = int(480 / frame_width * frame_height)  # 270
#
# ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)  # 高
# ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)



title='camera compare'
plt.ion()

cap.read()
cap.read()
cap.read()
cap.read()
ret, frame = cap.read()
temp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #
    m = mse(temp, gray)
    s = ssim(temp, gray)
    print("MSE: %.2f, SSIM: %.2f" % (m, s))
    #
    temp = gray.copy()
    continue

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(temp, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(gray, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()


