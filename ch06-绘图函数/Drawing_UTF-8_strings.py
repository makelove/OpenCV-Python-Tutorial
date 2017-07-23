# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 下午9:11
# @Author  : play4fun
# @File    : Drawing_UTF-8_strings.py
# @Software: PyCharm

"""
Drawing_UTF-8_strings.py:

https://fireant.github.io/misc/2017/01/28/ttf-opencv.html
"""

import cv2
import numpy as np

img = np.zeros((100, 300, 3), dtype=np.uint8)

ft = cv2.freetype.createFreeType2()  # 需要安装freetype模块 cv2' has no attribute 'freetype'
# ft.loadFontData(fontFileName='Ubuntu-R.ttf',id=0)
# ft.loadFontData(fontFileName='/usr/share/fonts/truetype/freefont/FreeSans.ttf',id=0)#不支持中文
# ft.loadFontData(fontFileName='/usr/share/fonts-droid/truetype/DroidSansFallback.ttf',id=0)#树莓派,搞定

#sudo apt-get install ttf-wqy-zenhei  #安装字体
ft.loadFontData(fontFileName='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', id=0)  # 文泉驿的开源中文字体


ft.putText(img=img,
           # text='Quick Fox',
           text='你好中文',
           org=(15, 70),
           fontHeight=60,
           color=(255, 255, 255),
           thickness=-1,
           line_type=cv2.LINE_AA,
           bottomLeftOrigin=True)

cv2.imwrite('freetype.png', img)
cv2.imshow('freetype', img)
cv2.waitKey(0)
