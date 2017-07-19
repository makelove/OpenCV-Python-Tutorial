# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 下午12:43
# @Author  : play4fun
# @File    : test_cvwm_videos.py
# @Software: PyCharm

"""
test_cvwm_videos.py:
"""

import cv2
from opencv_windows_management import opencv_windows_management

cvwm = opencv_windows_management()

cap = cv2.VideoCapture(0)
ret = cap.set(3, 640)
ret = cap.set(4, 480)

#
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.flip(frame, flipCode=1)
    cvwm.add('frame', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cvwm.add('gray', gray)

    #人脸识别
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("Detected ", len(faces), " face")
    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
        cvwm.add('face', face)

    cvwm.show()

    key = cv2.waitKey(delay=1)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
