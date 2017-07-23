# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 下午4:14
# @Author  : play4fun
# @File    : Pedestrian_Detection_video.py
# @Software: PyCharm

"""
Pedestrian_Detection_video.py:检测视频里的行人

视频网站
https://v.qq.com/x/page/t0501y6jtfi.html

"""

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import time

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--images", required=True, help="path to images directory")
# args = vars(ap.parse_args())

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#
cap = cv2.VideoCapture('videos/礼让斑马线！齐齐哈尔城市文明的伤！.mp4')
# cap = cv2.VideoCapture('../../data/TownCentreXVID.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('共有', num_frames, '帧')  # 共有 2499.0 帧

frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('高：', frame_height, '宽：', frame_width)  # 高： 480.0 宽： 640.0
# exit(0)


# 跳过多少帧
skips = 20

# loop over the image paths
# for imagePath in paths.list_images(args["images"]):
while cap.isOpened():

    # load the image and resize it to (1) reduce detection time
    # and (2) improve detection accuracy
    # image = cv2.imread(imagePath)

    ret, frame = cap.read()
    image = frame

    #
    current = cap.get(cv2.CAP_PROP_POS_FRAMES)
    if current % skips != 0:
        continue

    image = imutils.resize(image, width=min(400, image.shape[1]))
    orig = image.copy()

    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # show some information on the number of bounding boxes
    # filename = imagePath[imagePath.rfind("/") + 1:]
    # print("[INFO] {}: {} original boxes, {} after suppression".format(
    print("[INFO] {} original boxes, {} after suppression".format(len(rects), len(pick)))

    # show the output images
    cv2.imshow("Before NMS", orig)
    cv2.imshow("After NMS", image)
    cv2.moveWindow("After NMS", y=0, x=400)

    key = cv2.waitKey(delay=1)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
