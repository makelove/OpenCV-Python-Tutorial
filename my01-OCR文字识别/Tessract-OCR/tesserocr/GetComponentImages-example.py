# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 14:49
# @Author  : play4fun
# @File    : GetComponentImages-example.py.py
# @Software: PyCharm

"""
GetComponentImages-example.py:
"""

from PIL import Image
from tesserocr import PyTessBaseAPI, RIL

with PyTessBaseAPI() as api:
    # image = Image.open('/usr/src/tesseract/testing/phototest.tif')
    image = Image.open('phototest.tif')  # 图片有问题
    print(image.format, image.info, image.height, image.width)

    api.SetImage(image)
    boxes = api.GetComponentImages(RIL.TEXTLINE, True)
    print('Found {} textline image components.'.format(len(boxes)))
    for i, (im, box, _, _) in enumerate(boxes):
        # im is a PIL image object
        # box is a dict with x, y, w and h keys
        api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
        ocrResult = api.GetUTF8Text()
        conf = api.MeanTextConf()
        print(u"Box[{0}]: x={x}, y={y}, w={w}, h={h}, "
              "confidence: {1}, text: {2}").format(i, conf, ocrResult, **box)
