# -*- coding: utf-8 -*-

'''
扩展缩放

在缩放时我们推荐使用 cv2.INTER_AREA
在扩展时我们推荐使用 v2.INTER_CUBIC 慢) 和 v2.INTER_LINEAR。
默认情况下所有改变图像尺寸大小的操作使用的插值方法 是 cv2.INTER_LINEAR。

Resize(src, dst, interpolation=CV_INTER_LINEAR)
'''

import cv2
import numpy as np

img = cv2.imread('../data/messi5.jpg')
# 下面的 None 本应 是 出图像的尺寸 但是因为后边我们设置了缩放因子
# 因此这里为 None
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# OR
# 我们直接设置输出图像的尺寸 所以不用设置缩放因子
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

while True:
    cv2.imshow('resize', res)
    cv2.imshow('src img', img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows()
