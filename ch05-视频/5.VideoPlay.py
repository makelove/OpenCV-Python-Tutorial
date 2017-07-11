import numpy as np
import cv2

# cap = cv2.VideoCapture('vtest.avi')
cap = cv2.VideoCapture('output.avi')
# cap = cv2.VideoCapture('Minions_banana.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
