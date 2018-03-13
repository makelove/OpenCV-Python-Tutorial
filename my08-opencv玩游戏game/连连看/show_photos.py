# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 08:26
# @Author  : play4fun
# @File    : show_photos.py
# @Software: PyCharm

"""
show_photos.py:
"""

import cv2,pickle

with open('photo_mat','rb') as f:
    mat=pickle.load(f)

for x in mat:
    for y in x:
        cv2.imshow('mat',y)
        cv2.waitKey(10)
    cv2.waitKey(100)