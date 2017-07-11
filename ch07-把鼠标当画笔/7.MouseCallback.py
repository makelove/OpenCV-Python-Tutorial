# -*- coding: utf-8 -*-
import cv2
import numpy as np


# mouse callback function


def draw_circle(event, x, y, flags, param):  # 只用做一件事:在双击过的地方绘 制一个圆圈。
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    # if cv2.waitKey(20) & 0xFF == 27:
    #     break
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows()
