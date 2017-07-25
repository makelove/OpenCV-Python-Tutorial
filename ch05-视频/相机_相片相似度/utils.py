# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 23:37
# @Author  : play4fun
# @File    : utils.py
# @Software: PyCharm

"""
utils.py:
"""
import numpy as np

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err