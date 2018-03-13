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


def get_image_difference(image_1, image_2):  # 这个函数不行
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
            # image_difference = get_image_difference(y1, z1)
            res = cv2.matchTemplate(z1, y1, cv2.TM_CCOEFF_NORMED)
            # print(i, j, x, y, image_difference)
            print(i, j, x, y, res)
            # if abs(image_difference-1)>0.5:
            # if image_difference < 0.1:
            #     pairs.append((i, j, x, y, image_difference))
            if res[0][0] >= 0.9 and (i != x and j != y):
                pairs.append((i, j, x, y, res[0][0]))
        print('--------')


for i, x in enumerate(mat):
    for j, y in enumerate(x):
        compare(i, j, y)

print('--------')
print(pairs)#33对？
#[(0, 0, 5, 3, 0.93773538), (0, 3, 2, 6, 0.94418496), (0, 3, 3, 4, 0.97784418), (0, 3, 5, 6, 0.91531861), (0, 3, 7, 4, 0.90034771), (0, 4, 1, 5, 0.9859665), (0, 4, 2, 5, 0.97593749), (0, 4, 5, 7, 0.92510819), (1, 0, 2, 4, 0.95577663), (1, 0, 2, 5, 0.93438679), (1, 0, 3, 2, 0.98244762), (1, 0, 5, 1, 0.95950162), (1, 0, 5, 7, 0.9012484), (1, 0, 7, 3, 0.91213149), (1, 2, 4, 3, 0.97030866), (1, 3, 7, 5, 0.90350145), (1, 4, 3, 5, 0.92840946), (1, 4, 3, 6, 0.92976296), (1, 5, 5, 7, 0.93449652), (2, 1, 6, 4, 0.91386253), (2, 4, 5, 7, 0.95080549), (2, 5, 5, 7, 0.95228308), (3, 2, 5, 7, 0.94026983), (3, 2, 7, 3, 0.95594138), (3, 4, 5, 6, 0.96190572), (3, 4, 8, 7, 0.90763825), (4, 1, 7, 2, 0.95110172), (4, 3, 6, 6, 0.95759535), (5, 1, 7, 3, 0.97735828), (5, 2, 8, 3, 0.96606308), (5, 6, 8, 7, 0.92764288), (6, 0, 7, 3, 0.96886152), (7, 4, 8, 7, 0.93397516)]



#Test
# 1, 0, 1, 5
a = mat[1][0]
b = mat[1][5]
y1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
z1 = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
# image_difference = get_image_difference(y1, z1)
res = cv2.matchTemplate(z1, y1, cv2.TM_CCOEFF_NORMED)
print(1, 0, 1, 5, res)
