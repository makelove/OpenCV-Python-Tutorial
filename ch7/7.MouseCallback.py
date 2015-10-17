# -*- coding: utf-8 -*-
import cv2
import numpy as np


# mouse callback function


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image',0)
cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
