# -*-coding:utf8-*-#

__author__ = 'play4fun'
"""
create time:16/10/21 11:47
"""
# Orientation and script detection (OSD)

from PIL import Image
from tesserocr import PyTessBaseAPI, PSM

with PyTessBaseAPI(psm=PSM.AUTO_OSD) as api:
    # image = Image.open("/usr/src/tesseract/testing/eurotext.tif")#No such file
    # image = Image.open("eurotext.tif")
    image = Image.open('phototest.tif')
    api.SetImage(image)
    api.Recognize()

    it = api.AnalyseLayout()
    orientation, direction, order, deskew_angle = it.Orientation()
    print("Orientation: {:d}".format(orientation))
    print("WritingDirection: {:d}".format(direction))
    print("TextlineOrder: {:d}".format(order))
    print("Deskew angle: {:.4f}".format(deskew_angle))
    #
    ocrResult = api.GetUTF8Text()
    print('result:\n',ocrResult)
