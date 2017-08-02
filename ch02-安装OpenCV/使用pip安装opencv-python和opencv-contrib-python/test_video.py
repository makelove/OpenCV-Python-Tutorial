# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 10:46
# @Author  : play4fun
# @File    : test_video.py
# @Software: PyCharm

"""
test_video.py:
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('../../data/vtest.avi')
# cap = cv2.VideoCapture('output.avi')
# cap = cv2.VideoCapture('Minions_banana.mp4')


# 帧率
fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
# 总共有多少帧
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('共有', num_frames, '帧')
#
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('高：', frame_height, '宽：', frame_width)

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 第0帧
print('当前帧数', FRAME_NOW)  # 当前帧数 0.0

# 读取指定帧,对视频文件才有效，对摄像头无效？？
frame_no = 121
cap.set(1, frame_no)  # Where frame_no is the frame you want
ret, frame = cap.read()  # Read the frame
# cv2.imshow('frame_no'+str(frame_no), frame)

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)
print('当前帧数', FRAME_NOW)  # 当前帧数 122.0

plt.imshow(thresh,cmap='gray')
plt.show()