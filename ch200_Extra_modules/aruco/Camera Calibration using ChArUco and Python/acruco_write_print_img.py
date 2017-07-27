# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 15:39
# @Author  : play4fun
# @File    : acruco_write_print_img.py
# @Software: PyCharm

"""
acruco_write_print_img.py:
"""

import cv2
import numpy as np

num = 5

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# board = cv2.aruco.CharucoBoard_create(9, 9, .025, .0125, dictionary)
board = cv2.aruco.CharucoBoard_create(num, num, .025, .0125, dictionary)
# img = board.draw((200 * 9, 200 * 9))
img = board.draw((200 * num, 200 * num))

# Dump the calibration board to a file
cv2.imwrite(f'charuco_{num}x{num}.png', img)
# 用打印机打印出来
# 或放在平板电脑里
