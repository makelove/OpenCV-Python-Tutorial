# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 上午11:16
# @Author  : play4fun
# @File    : 11.ipython.py
# @Software: PyCharm

"""
11.ipython.py:
"""

import cv2
import numpy as np
'''

In [10]: x = 5
In [11]: %timeit y=x**2
10000000 loops, best of 3: 73 ns per loop
In [12]: %timeit y=x*x
10000000 loops, best of 3: 58.3 ns per loop
In [15]: z = np.uint8([5])
In [17]: %timeit y=z*z
1000000 loops, best of 3: 1.25 us per loop
In [19]: %timeit y=np.square(z)
1000000 loops, best of 3: 1.16 us per loop
#Python 的标量运算比 Nump 的标量运算 快。
#对于仅包含一两个 元素的操作 Python 标量比 Numpy 的数组 快。
#但是当数组稍微大一点时 Numpy 就会胜出了
'''

'''
In [35]: %timeit z = cv2.countNonZero(img)
100000 loops, best of 3: 15.8 us per loop
In [36]: %timeit z = np.count_nonzero(img)
1000 loops, best of 3: 370 us per loop
#OpenCV 的函数是 Numpy 函数的 25 倍

#一般情况下 OpenCV 的函数 比 Numpy 函数快。所以对于相同的操
作最好使用 OpenCV 的函数。当然也有例外 尤其是当使用 Numpy 对 图  而 复制   操作时
'''

'''
有些技术和编程方法可以 我们最大的发挥 Python 和 Numpy 的威力。 
我们  仅仅提一下相关的,你可以超链接查找更多 细信息。
我们 要说的最重要的一点是：
 先用简单的方式实现你的算法(结果正确最重要)
 当结果正确后 再使用上面的提到的方法找到程序的瓶 来优化它。
1. 尽量避免使用循环 尤其双层三层循环 它们天生就是 常慢的。
2. 算法中尽量使用向量操作 因为 Numpy 和 OpenCV  对向量操作了优化。
3. 利用高速缓存一致性。
4. 没有必要的话就不要复制数组。使用视图来代替复制。数组复制是非常浪费资源的。
'''