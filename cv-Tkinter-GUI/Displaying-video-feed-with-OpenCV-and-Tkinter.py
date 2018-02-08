# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 16:09
# @Author  : play4fun
# @File    : Displaying a video feed with OpenCV and Tkinter.py
# @Software: PyCharm

"""
Displaying a video feed with OpenCV and Tkinter.py:
https://www.pyimagesearch.com/2016/05/30/displaying-a-video-feed-with-opencv-and-tkinter/

"""

# import the necessary packages
from __future__ import print_function
from photoboothapp import PhotoBoothApp
from imutils.video import VideoStream
import argparse
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1,
                help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# start the app
pba = PhotoBoothApp(vs, args["output"])
pba.root.mainloop()
