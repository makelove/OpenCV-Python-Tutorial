# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午9:56
# @Author  : play4fun
# @File    : 1-fastNlMeansDenoisingColored.py
# @Software: PyCharm

"""
1-fastNlMeansDenoisingColored.py:
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('die.png')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)

dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
# dst2=cv2.cvtColor(dst,code=cv2.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
# plt.subplot(122), plt.imshow(dst2)
plt.show()
