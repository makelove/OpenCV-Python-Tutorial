# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午7:35
# @Author  : play4fun
# @File    : 2-英文字母的OCR.py
# @Software: PyCharm

"""
2-英文字母的OCR.py:
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
data = np.loadtxt('../data/letter-recognition.data', dtype='float32', delimiter=',',
                  converters={0: lambda ch: ord(ch) - ord('A')})#20000个
# split the data to two, 10000 each for train and test
train, test = np.vsplit(data, 2)
# split trainData and testData to features and responses
responses, trainData = np.hsplit(train, [1])
labels, testData = np.hsplit(test, [1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=5)

correct = np.count_nonzero(result == labels)
accuracy = correct * 100.0 / 10000
print(accuracy)
#准确率 到了 93.22%。同样你可以  增加训练样本的数量来提 准确率。

with np.load('knn_data_alphabet.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']
    test = data['test']
    test_labels = data['test_labels']

#怎样预测字母？跟预测数字的一样
