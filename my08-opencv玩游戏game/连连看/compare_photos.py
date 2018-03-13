# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 08:30
# @Author  : play4fun
# @File    : compare_photos.py
# @Software: PyCharm

"""
compare_photos.py:
"""

import cv2, pickle

with open('photo_mat', 'rb') as f:
    mat = pickle.load(f)

pairs = []  # 配对好的
lenX = 9  # 行
lenY = 8  # 列


def get_image_difference(image_1, image_2):#这个函数不行
    first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

    img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match

    # taking only 10% of histogram diff, since it's less accurate than template method
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff


def compare(i, j, img):
    for x in range(lenX):
        if x < i:
            continue
        for y in range(lenY):
            if y < j:
                continue
            z = mat[x][y]
            # 图片相似度
            y1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            z1 = cv2.cvtColor(z, cv2.COLOR_BGR2GRAY)
            image_difference = get_image_difference(y1, z1)
            print(i, j, x, y, image_difference)
            # if abs(image_difference-1)>0.5:
            if image_difference < 0.1:
                pairs.append((i, j, x, y, image_difference))
        print('--------')


for i, x in enumerate(mat):
    for j, y in enumerate(x):
        compare(i, j, y)

print('--------')
# print(pairs)



# 1, 0, 1, 5
a = mat[1][0]
b = mat[1][5]
y1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
z1 = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
image_difference = get_image_difference(y1, z1)
print(1, 0, 1, 5, image_difference)
