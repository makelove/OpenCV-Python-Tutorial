# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 19:38
# @Author  : play4fun
# @File    : kinect.py
# @Software: PyCharm

"""
kinect.py:
"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np

from .camera import Camera
from .draw import Gravity, put_text


def main():
    def callback(frame, depth, fps):
        # Normalize the depth for representation
        min, max = depth.min(), depth.max()
        depth = np.uint8(255 * (depth - min) / (max - min))

        # Unable to retrieve correct frame, it's still depth here
        put_text(frame, "{1}x{0}".format(*frame.shape), Gravity.TOP_LEFT)
        put_text(depth, "{1}x{0}".format(*depth.shape), Gravity.TOP_LEFT)

        put_text(depth, "%.1f" % fps, Gravity.TOP_RIGHT)

        cv2.imshow('frame', frame)
        cv2.imshow('depth', depth)

    with Camera(cv2.CAP_OPENNI2) as cam:
        print("Camera: %dx%d, %d" % (
            cam.get(cv2.CAP_OPENNI_IMAGE_GENERATOR + cv2.CAP_PROP_FRAME_WIDTH),
            cam.get(cv2.CAP_OPENNI_IMAGE_GENERATOR + cv2.CAP_PROP_FRAME_HEIGHT),
            cam.get(cv2.CAP_OPENNI_IMAGE_GENERATOR + cv2.CAP_PROP_FPS)))
        cam.capture(callback, False)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


# Using Kinect and other OpenNI compatible depth sensors:
#   http://docs.opencv.org/master/d7/d6f/tutorial_kinect_openni.html
# OpenCV Python unable to access correct OpenNI device channels:
#   https://github.com/opencv/opencv/issues/4735