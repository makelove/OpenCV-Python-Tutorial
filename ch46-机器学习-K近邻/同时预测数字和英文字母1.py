# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 17:59
# @Author  : play4fun
# @File    : 同时预测数字和英文字母1.py
# @Software: PyCharm

"""
同时预测数字和英文字母1.py:
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

with np.load('knn_data_alphabet.npz') as data:
    print(data.files)
    train_alphabet = data['train_alphabet']
    train_labels_alphabet = data['train_labels_alphabet']
    test_alphabet = data['test_alphabet']
    test_labels_alphabet = data['test_labels_alphabet']

# shape不一致，无法合并
# train.shape #(2500, 400)
# train_alphabet.shape#(10000, 17)
# print('合并-数字-字母数据')
# train = np.append(train, train_alphabet)
# tratrain_labelsin = np.append(train_labels,train_labels_alphabet)
# test = np.append(test, test_alphabet)
# test_labels = np.append(test_labels, test_labels_alphabet)

print('加载KNN,数据')
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
knn.train(train_alphabet, cv2.ml.ROW_SAMPLE, train_labels_alphabet)

ret, result, neighbours, dist = knn.findNearest(
    test, k=5)# shape不一致
#出错，knearest.cpp:325: error: (-215) test_samples.type() == CV_32F && test_samples.cols == samples.cols in function findNearest