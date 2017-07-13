'''
假如你的目标对 只在图像中出现了很多次怎么办呢
函数 cv.imMaxLoc() 只会给出最大值和最小值。此时 我们就 使用阈值了。
在下 的例子中我们 经典游戏 Mario 的一张截屏图片中找到其中的硬币

'''

import cv2
import numpy as np

# from matplotlib import pyplot as plt

img_rgb = cv2.imread('../data/mario.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('../data/mario_coin.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
print(len(loc))

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    print("rectangle 1")

# cv2.imwrite('res.png',img_rgb)
cv2.imshow("result", img_rgb)
cv2.waitKey(0)
