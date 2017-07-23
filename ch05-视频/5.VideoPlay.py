import numpy as np
import cv2

cap = cv2.VideoCapture('../data/vtest.avi')
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

# 读取指定帧
frame_no = 121
cap.set(1, frame_no)  # Where frame_no is the frame you want
ret, frame = cap.read()  # Read the frame
cv2.imshow('frame', frame)

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)
print('当前帧数', FRAME_NOW)  # 当前帧数 122.0

while cap.isOpened():
    ret, frame = cap.read()
    FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 当前帧数
    print('当前帧数', FRAME_NOW)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
