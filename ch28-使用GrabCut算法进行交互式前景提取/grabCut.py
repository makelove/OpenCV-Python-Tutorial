# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-25 下午12:20


img - 输入图像
• mask-掩模图像 用来确定 些区域是背景 前景 可能是前景/背景等。 可以 置为 cv2.GC_BGD,cv2.GC_FGD,cv2.GC_PR_BGD,cv2.GC_PR_FGD  或者直接 入 0,1,2,3 也 。
• rect - 包含前景的矩形 格式为 (x,y,w,h)
• bdgModel, fgdModel - 算法内 使用的数组. 你只  创建两个大
小为 (1,65) 数据类型为 np.float64 的数组。
• iterCount - 算法的迭代次数
• mode可以 置为cv2.GC_INIT_WITH_RECT或cv2.GC_INIT_WITH_MASK  也可以联合使用。 是用来确定我们  修改的方式 矩形模式或者掩模
模式。
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/messi5.jpg')

mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 450, 290)

# 函数的返回值是更新的 mask, bgdModel, fgdModel
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount=5, mode=cv2.GC_INIT_WITH_RECT)
#迭代 5 次

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

plt.imshow(img), plt.colorbar(), plt.show()
