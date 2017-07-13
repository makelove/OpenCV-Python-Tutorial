# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午3:13
# @Author  : play4fun
# @File    : surf.py
# @Software: PyCharm

"""
surf.py:SURF加速稳健特征，加速版的SIFT

积分图像的一大特点是 计算图像中某个窗 口内所有像素和时，计算量的大小与窗口大小无关

"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('fly.png', 0)
# Create SURF object. You can specify params here or later. # Here I set Hessian Threshold to 400
# surf = cv2.SURF(400)
surf = cv2.xfeatures2d.SURF_create(400)

# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img, None)
len(kp)  # 699

# 提高Hessian 的阈值
# Check present Hessian threshold
print(surf.getHessianThreshold())
# 400.0
# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.setHessianThreshold(50000)
# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img, None)
print(len(kp))
# 47
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)

plt.imshow(img2)
plt.show()

# 最后我们再看看关键点描述符的大小 如果是 64 维的就改成 128 维。

# Find size of descriptor
print(surf.descriptorSize())
# 64
# That means flag, "extended" is False.
print(surf.getExtended())
# False
# So we make it to True to get 128-dim descriptors.
surf.extended = True
kp, des = surf.detectAndCompute(img, None)
print(surf.descriptorSize())
# 128
print(des.shape)
# (47, 128)

# 接下来要做的就是匹配了 我们会在后讨论。
