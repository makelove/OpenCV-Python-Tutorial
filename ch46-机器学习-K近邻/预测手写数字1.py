# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 11:57
# @Author  : play4fun
# @File    : 预测手写数字1.py
# @Software: PyCharm

"""
预测手写数字1.py:

验证码
https://login.bthhotels.com/
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

with np.load('knn_data_num.npz') as data:
    print(data.files)  # ['train', 'train_labels', 'test', 'test_labels']
    train = data['train']
    train_labels = data['train_labels']
    test = data['test']
    test_labels = data['test_labels']

print('加载KNN,数据')
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

# 加载相片
print('加载相片')
img2 = cv2.imread('2.png', 0)
gray2 = cv2.resize(img2, (20, 20))
# gray2=gray2.reshape((400,))
gray21 = gray2.reshape((-1, 400)).astype(np.float32)

img6 = cv2.imread('6.png', 0)
gray6 = cv2.resize(img6, (20, 20))
# gray2=gray2.reshape((400,))
gray61 = gray6.reshape((-1, 400)).astype(np.float32)

g2 = np.append(gray21, gray61)
g3 = g2.reshape((2, 400))

# 预测
retval, results = knn.predict(g3)
print(retval, results)  # 不准确
# (0.0, array([[ 0.],
#         [ 5.]], dtype=float32))
