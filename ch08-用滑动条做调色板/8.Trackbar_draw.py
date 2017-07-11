# -*- coding: utf-8 -*-
import cv2
import numpy as np


def nothing(x):
    pass


# 当鼠标按下时变为 True
drawing = False
# 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。 mode=True
ix, iy = -1, -1

'''
cv2.getTrackbarPos() 函数的第一个参数是滑动条的名字 
第二个参数 是滑动条被放置窗口的名字 
第三个参数是滑动条的默认位置。
第四个参数是滑动条的最大值 
第五个函数是回调函数， 每次滑动条的滑动都会调用回调函 数。
回调函数通常都会含有一个默认参数 就是滑动条的位置
'''


# 创建回调函数
def draw_circle(event, x, y, flags, param):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    color = (b, g, r)

    global ix, iy, drawing, mode
    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 当鼠标左键按下并移动是绘制图形。event 可以查看移动,flag 查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                # 绘制圆圈,小圆点连在一起就成了线,3 代表了笔画的粗细
                cv2.circle(img, (x, y), 3, color, -1)
                # 下面注释掉的代码是起始点为圆心,起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)

                # 当鼠标松开停止绘画。
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # if mode==True:
        #     cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
        #     cv2.circle(img,(x,y),5,(0,0,255),-1)


img = np.zeros((512, 512, 3), np.uint8)
mode = False

cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1)  # & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord("q"):
        break
