# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:52
# @Author  : play4fun
# @File    : lian-1.py
# @Software: PyCharm

"""
lian-1.py:切割图片
"""

import cv2

filename = 'lianliankan2.png'
img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

size = img.shape
print('size:', size)  # (627, 554, 3)
width = size[1]
height = size[0]

cv2.imshow('src', img)
cv2.waitKey(0)

# 分割，9行627，8列554
x1 = 0
y1 = 0
xp = int(height / 9)
yp = int(width / 8)
mat=[]
for x2 in range(xp, height, xp):
    pl=[]
    for y2 in range(yp, width, yp):
        cut = img[x1:x2, y1:y2]
        cv2.imshow('cut', cut)
        cv2.waitKey(10)

        y1 = y2
        #
        pl.append(cut)
    cv2.waitKey(100)
    y1 = 0
    x1 = x2
    #
    mat.append(pl)

cv2.waitKey(0)
cv2.destroyAllWindows()

#
import pickle
with open('photo_mat','wb') as f:
    pickle.dump(mat,f)