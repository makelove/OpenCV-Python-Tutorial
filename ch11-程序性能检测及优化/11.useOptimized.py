# -*- coding: utf-8 -*-
import cv2
import numpy as np

'''
OpenCV 中的默认优化
在编译时 优化是 默认开启的。因此 OpenCV   的就是优化后的代码 
如果你把优化 关闭的 就只能执行低效的代码了。
你可以使用函数 cv2.useOptimized() 来查看优化是否 开启了 
使用函数 cv2.setUseOptimized() 来开启优化
'''
# check if optimization is enabled
"""
In [5]: cv2.useOptimized()
Out[5]: True
In [6]: %timeit res = cv2.medianBlur(img,49)
10 loops, best of 3: 34.9 ms per loop
# Disable it
In [7]: cv2.setUseOptimized(False)
In [8]: cv2.useOptimized()
Out[8]: False
In [9]: %timeit res = cv2.medianBlur(img,49)
#优化后中值滤波的速度是原来的两倍
"""
print(cv2.useOptimized())
cv2.setUseOptimized(False)
print(cv2.useOptimized())