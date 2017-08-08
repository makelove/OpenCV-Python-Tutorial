# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 11:57
# @Author  : play4fun
# @File    : 预测手写数字1.py
# @Software: PyCharm

"""
预测手写数字1.py:
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

with np.load('knn_data.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']
    test = data['test']
    test_labels = data['test_labels']

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)