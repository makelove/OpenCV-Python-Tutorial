# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 下午7:07
# @Author  : play4fun
# @File    : draw_opencv_logo.py
# @Software: PyCharm

"""
draw_opencv_logo.py:Try to create the logo of OpenCV using drawing functions available in OpenCV.
"""

import numpy as np
import cv2  # 3.0.0-dev
import math

r1 = 70
r2 = 30

ang = 60

d = 170
h = int(d / 2 * math.sqrt(3))

dot_red = (256, 128)
dot_green = (int(dot_red[0] - d / 2), dot_red[1] + h)
dot_blue = (int(dot_red[0] + d / 2), dot_red[1] + h)

# tan = float(dot_red[0]-dot_green[0])/(dot_green[1]-dot_red[0])
# ang = math.atan(tan)/math.pi*180

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (0, 0, 0)

full = -1

img = np.zeros((512, 512, 3), np.uint8)
# img = np.ones((512, 512, 3), np.uint8)

cv2.circle(img, dot_red, r1, red, full)
cv2.circle(img, dot_green, r1, green, full)
cv2.circle(img, dot_blue, r1, blue, full)
cv2.circle(img, dot_red, r2, black, full)
cv2.circle(img, dot_green, r2, black, full)
cv2.circle(img, dot_blue, r2, black, full)

cv2.ellipse(img, dot_red, (r1, r1), ang, 0, ang, black, full)
cv2.ellipse(img, dot_green, (r1, r1), 360 - ang, 0, ang, black, full)
cv2.ellipse(img, dot_blue, (r1, r1), 360 - 2 * ang, ang, 0, black, full)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text='OpenCV', org=(15, 450), fontFace=font, fontScale=4, color=(255, 255, 255), thickness=10)#text,

cv2.imwrite("opencv_logo.png", img)
# cv2.imwrite("opencv_logo2.png", img)
