# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 19:37
# @Author  : play4fun
# @File    : draw.py
# @Software: PyCharm

"""
draw.py:
"""

import cv2


FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1
THICKNESS = 1


class Gravity:
    TOP_LEFT        = 1
    TOP_RIGHT       = 2
    BOTTOM_LEFT     = 3
    BOTTOM_RIGHT    = 4


def put_text(img, text, gravity, margin=10):
    h, w = img.shape[:2]
    # getTextSize, result: ((width, height), baseline)
    x, y = cv2.getTextSize(text, FONT_FACE, FONT_SCALE, THICKNESS)[0];
    # putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
    org = {
        Gravity.TOP_LEFT:       (margin, margin+y),
        Gravity.TOP_RIGHT:      (w-margin-x, margin+y),
        Gravity.BOTTOM_LEFT:    (margin, h-margin),
        Gravity.BOTTOM_RIGHT:   (w-margin-x, h-margin),
    }.get(gravity, (margin, margin+y))
    cv2.putText(img, text, org, FONT_FACE, FONT_SCALE,
        (255,255,255), THICKNESS, cv2.LINE_AA)