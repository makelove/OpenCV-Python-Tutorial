# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 12:33
# @Author  : play4fun
# @File    : knn-find_nearest.py
# @Software: PyCharm

"""
knn-find_nearest.py:
http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Machine_Learning_Classification_K-nearest_neighbors_k-NN.php
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# plot Reds
red = trainData[responses.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

# plot Blues
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

# CvKNearest instance
# knn = cv2.KNearest()
knn = cv2.ml.KNearest_create()
# trains the model
knn.train(trainData, responses)#TODO
#TypeError: only length-1 arrays can be converted to Python scalars


# New sample : (x,y)
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

# Finds the 3nearest  neighbors and predicts responses for input vectors
ret, results, neighbours, dist = knn.find_nearest(newcomer, 3)

print("result: ", results, "\n")
print("neighbours: ", neighbours, "\n")
print("distance: ", dist)

plt.show()
