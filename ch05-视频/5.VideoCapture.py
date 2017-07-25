# -*- coding: utf-8 -*-
"""
Created on Fri Jan 3 21:06:22 2014

@author: duan
 """
'''
 注意 当你的程序报错时 你 先检查的是你的摄像头是否能够在其他程 序中正常工作 比如 linux 下的 Cheese 。
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # 一般的笔 本电脑 有内置摄像头。所以参数就是 0。你可以  设置成 1 或 者其他的来 择别的摄像头

'''
你可以使用函数 cap.get(propId) 来获得  的一些参数信息。   
propId 可以是 0 到 18 之 的任何整数。

其中的一些值可以使用 cap.set(propId,value) 来修改 value 就是 你想  置成的新值。
例如 我可以使用 cap.get(3) cv2.CAP_PROP_FRAME_WIDTH和 cap.get(4) cv2.CAP_PROP_FRAME_HEIGHT来查看每一帧的宽和高。   
默认情况下得到的值是 640X480。但是我可以使用 ret=cap.set(3,320) 和 ret=cap.set(4,240) 来把宽和高改成 320X240。
'''
# ret=cap.set(3,320)
# ret=cap.set(4,240)

# ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)#避免计算量过大
# ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 270)#
#等比缩放
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)#4 ，720
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)#3   ，1280
frame_height=int(480/frame_width*frame_height)#270
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)#高
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)



# while (True):
while cap.isOpened():  # 检查是否成功初始化，否则就 使用函数 cap.open()
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret 返回一个布尔值 True/False
    # print('frame shape:',frame.shape)#(720, 1280, 3)

    frame = cv2.flip(frame, flipCode=1)  # 左右翻转,使用笔记本电脑摄像头才有用。
    # flipCode：翻转方向：1：水平翻转；0：垂直翻转；-1：水平垂直翻转

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    # if cv2.waitKey(1) & 0xFF == ord('q'):#不行
    #     break
    key = cv2.waitKey(delay=1)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
