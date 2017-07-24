# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 下午5:03
# @Author  : play4fun
# @File    : blob_camera.py
# @Software: PyCharm

"""
blob_camera.py:
"""

import cv2
import numpy as np

# Read image
# im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

cap = cv2.VideoCapture(0)
while cap.isOpened():  # 检查是否成功初始化，否则就 使用函数 cap.open()
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect blobs.
    keypoints = detector.detect(gray)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)

    key = cv2.waitKey(delay=1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
