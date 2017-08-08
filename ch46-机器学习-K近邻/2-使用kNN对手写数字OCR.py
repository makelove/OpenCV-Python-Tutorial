# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午7:32
# @Author  : play4fun
# @File    : 2-使用kNN对手写数字OCR.py
# @Software: PyCharm

"""
2-使用kNN对手写数字OCR.py:
"""

# 准备数据

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)
# Now we prepare train_data and test_data.
train = x[:, :50].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)

# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()

# Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size
print('准确率', accuracy)  # 准确率91.76%

''''''
# save the data
np.savez('knn_data.npz', train=train, train_labels=train_labels,test=test,test_labels=test_labels)
# Now load the data
with np.load('knn_data.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']
    test = data['test']
    test_labels = data['test_labels']


#TODO 怎样预测数字？
retval, results=knn.predict(test[3:5])
# Docstring: predict(samples[, results[, flags]]) -> retval, results
