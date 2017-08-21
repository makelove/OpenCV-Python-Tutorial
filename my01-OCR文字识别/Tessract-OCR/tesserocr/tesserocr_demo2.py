# -*-coding:utf8-*-#

__author__ = 'play4fun'
"""
create time:16/10/21 11:47
"""

import tesserocr
from PIL import Image

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('sample.jpg')
print(tesserocr.image_to_text(image))  # print ocr text from image
# or
print(tesserocr.file_to_text('sample.jpg'))
