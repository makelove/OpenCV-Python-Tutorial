'''
http://www.technicdynamic.com/2017/08/28/python-motion-detection-with-opencv-simple/

'''

import cv2  # importing Python OpenCV
from datetime import datetime  # importing datetime for naming files w/ timestamp


def diffImg(t0, t1, t2):  # Function to calculate difference between images.
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


threshold = 81500  # Threshold for triggering "motion detection"
cam = cv2.VideoCapture(0)  # Lets initialize capture on webcam

winName = "Movement Indicator"  # comment to hide window
cv2.namedWindow(winName)  # comment to hide window

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
# Lets use a time check so we only take 1 pic per sec
timeCheck = datetime.now().strftime('%Ss')

while True:
    cv2.imshow(winName, cam.read()[1])  # comment to hide window
    if cv2.countNonZero(diffImg(t_minus, t, t_plus)) > threshold and timeCheck != datetime.now().strftime('%Ss'):
        dimg = cam.read()[1]
        # cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', dimg)
    timeCheck = datetime.now().strftime('%Ss')
    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    key = cv2.waitKey(10)
    if key == ord('q'):
        cv2.destroyWindow(winName)  # comment to hide window
        break
