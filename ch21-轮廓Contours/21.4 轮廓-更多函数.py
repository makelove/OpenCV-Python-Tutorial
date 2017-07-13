# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午8:47
# @Author  : play4fun
# @File    : 21.4 轮廓-更多函数.py
# @Software: PyCharm

"""
21.4 轮廓-更多函数.py:
"""

import cv2
import numpy as np

'''
Point Polygon Test
求 图像中的一个点到一个对  廓的最短 离。如果点在 廓的外    回值为 。如果在 廓上  回值为 0。如果在 廓内   回值为正。
下 我们以点 50 50 为例 

dist = cv2.pointPolygonTest(cnt,(50,50),True)

此函数的第三个参数是 measureDist。如果 置为 True 就会 算最 短 离。如果是 False 只会判断 个点与 廓之 的位置关系  回值为 +1 -1 0 

 注意 如果你不  知 具体 离 建 你将第三个参数 为 False  这样速度会提  2 到 3 倍。
'''
