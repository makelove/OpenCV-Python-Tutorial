#!/usr/bin/env python

'''
Video histogram sample to show live histogram of video

Keys:
    ESC    - exit

'''

import numpy as np
import cv2

# built-in modules
import sys

# local modules
import video

if __name__ == '__main__':

    # 构建 HSV颜色地图
    hsv_map = np.zeros((180, 256, 3), np.uint8)
    # np.indices 可以 回由数组索引构建的新数组。 例如 np.indices 3,2  其中 3,2 为原来数组的维度  和列。  回值 先看 入的参数有几维  3,2 有 2 维 所以从 出的结果应 是 [[a],[b]], 其中包含两个 3   2 列数组。 第二看每一维的大小 第一维为 3, 所以 a 中的值就 0 到 2 最大索引数  a 中的每一个值就是它的 索引 同样的方法得到 b 列索引
    # 结果就是
    #  array([[[0, 0],
    #      [1, 1],
    #   [2, 2]],
    #     [[0, 1],
    #      [0, 1],
    #      [0, 1]]])
    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:, :, 0] = h
    hsv_map[:, :, 1] = s
    hsv_map[:, :, 2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
    cv2.imshow('hsv_map', hsv_map)

    cv2.namedWindow('hist', 0)
    hist_scale = 10


    def set_scale(val):
        global hist_scale
        hist_scale = val


    cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

    try:
        fn = sys.argv[1]
    except:
        fn = 0
    cam = video.create_capture(fn, fallback='synth:bg=../data/baboon.jpg:class=chess:noise=0.05')

    while True:
        flag, frame = cam.read()
        cv2.imshow('camera', frame)
        # 图像 字塔
        #   图像 字塔 低分 率 但不会对直方图有太大影响。
        # 但 种低分 率 可以很好抑制噪声 从而去 孤立的小点对直方图的影响
        small = cv2.pyrDown(frame)

        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
        dark = hsv[..., 2] < 32
        hsv[dark] = 0
        h = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

        h = np.clip(h * 0.005 * hist_scale, 0, 1)
        vis = hsv_map * h[:, :, np.newaxis] / 255.0
        cv2.imshow('hist', vis)

        ch = cv2.waitKey(1)
        if ch == ord('q'):
            break
    cv2.destroyAllWindows()
