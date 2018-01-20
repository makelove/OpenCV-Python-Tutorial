# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 17:15
# @Author  : play4fun
# @File    : 颜色转换.py
# @Software: PyCharm

"""
颜色转换.py:
"""
import cv2


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


temp = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)#灰色转RGB