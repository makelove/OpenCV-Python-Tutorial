# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 10:23
# @Author  : play4fun
# @File    : test_opencv_contrib_python.py
# @Software: PyCharm

"""
test_opencv_contrib_python.py:
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt
from time import sleep

# 运行之前，检查cascade文件路径是否在你的电脑上
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

# img = cv2.imread('../../data/sachin.jpg')
# img = cv2.imread('../../data/kongjie_hezhao.jpg')
img = cv2.imread('../../data/airline-stewardess-bikini.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)


faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print("Detected ", len(faces), " face")

plt.ion()
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()
        # cv2.waitKey(500)
        plt.pause(2)
        # sleep(2)
    # sleep(2)
    # cv2.waitKey(500)
    plt.pause(2)

# plt.show()
plt.show(block=True)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite('face_recognize.jpg', img)