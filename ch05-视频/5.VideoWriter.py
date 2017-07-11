import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = 640
ret = cap.set(3, width)
height = 480
ret = cap.set(4, height)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # opencv 3.0
# Error: 'module' object has no attribute 'VideoWriter_fourcc'
# fourcc=cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
#jpeg,h263,'m', 'p', '4', 'v'

#
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:

        frame = cv2.resize(frame, (640, 480))

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)

    else:
        break

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
