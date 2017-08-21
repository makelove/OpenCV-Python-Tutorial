# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 13:26
# @Author  : play4fun
# @File    : 获取验证码-然后识别.py
# @Software: PyCharm

"""
获取验证码-然后识别.py:
"""

from io import BytesIO
from PIL import Image
import requests
from tesserocr import PyTessBaseAPI
import tesserocr
import numpy as np
import cv2


user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
headers = {'User-Agent': user_agent}


url = 'http://www.bjsuperpass.com/captcha.svl?d=1503144107405'
rs = requests.get(url, headers=headers, timeout=10)
print('获取公交一卡通网站的验证码',rs.status_code)

print('用BytesIO导入到Image，Numpy，Opencv')
s1 = BytesIO(rs.content)  # img = Image.open(BytesIO(resp.read()))
#
img = Image.open(s1)
img = img.convert("RGB")
im=np.array(img)
cv2.imshow('src',im)
cv2.waitKey(0)
cv2.imwrite('captcha.jpg',im)


ocr = PyTessBaseAPI()
# ocr.Init(".", "eng", tesseract.OEM_DEFAULT)
ocr.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
# ocr.SetPageSegMode(tesseract.PSM_AUTO)
# ocr.SetImage(img)

print('验证码是',tesserocr.image_to_text(img))