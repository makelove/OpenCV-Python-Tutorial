# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 19:34
# @Author  : play4fun
# @File    : kinect_test.py
# @Software: PyCharm

"""
kinect_test.py:
https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/

安装驱动
sudo apt install python-freenect
python2.7  kinect_test.py
第二次启动，成功！
"""

# import the necessary modules
import freenect
import cv2
import numpy as np


# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


# function to get depth image from kinect
def get_depth():
    array, _ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array


if __name__ == "__main__":
    print 'start'
    while 1:
        # get a frame from RGB camera
        frame = get_video()
        print 'frame',type(frame)
        # get a frame from depth sensor
        depth = get_depth()
        print 'depth', type(depth)
        # display RGB image
        cv2.imshow('RGB image', frame)
        # display depth image
        cv2.imshow('Depth image', depth)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
