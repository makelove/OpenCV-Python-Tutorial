# -*- coding: utf-8 -*-
# @Time    : 2017/8/6 11:32
# @Author  : play4fun
# @File    : matchTemplate_credit_card_num1.py
# @Software: PyCharm

"""
matchTemplate_credit_card_num1.py:

http://www.pyimagesearch.com/2017/07/17/credit-card-ocr-with-opencv-and-python/

python ocr_template_match.py --reference ocr_a_reference.png --image images/credit_card_04.png

Credit Card Type: Visa
Credit Card #: 4000123456789010


检测图像中信用卡的位置。
本地化四位数字，与信用卡上十六位数相关。
应用OCR来识别信用卡上的十六位数字。
识别信用卡类型（即Visa，万事达卡，美国运通等）。

"""

# import the necessary packages
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments解析命令行参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-r", "--reference", required=True,
                help="path to reference OCR-A image")
args = vars(ap.parse_args())

# define a dictionary that maps the first digit of a credit card
# number to the credit card type定义信用卡类型
FIRST_NUMBER = {
    '0': 'None',
    "3": "American Express",
    "4": "Visa",
    "5": "MasterCard",
    "6": "Discover Card"
}

# load the reference OCR-A image from disk, convert it to grayscale,
# and threshold it, such that the digits appear as *white* on a
# *black* background
# and invert it, such that the digits appear as *white* on a *black*
ref = cv2.imread(args["reference"])
ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]

cv2.imshow('ref', ref)
cv2.waitKey(0)

'''
# find contours in the OCR-A image (i.e,. the outlines of the digits)
# sort them from left to right, and initialize a dictionary to map
# digit name to the ROI
# refCnts = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#有问题
refCnts = cv2.findContours(ref.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# refCnts = refCnts[0] if imutils.is_cv2() else refCnts[1]
refCnts = refCnts[1]
print('len cnt:',len(refCnts))
refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]#排列轮廓，没意义
print('sort_contours len cnt:',len(refCnts))
digits = {}

# 循环浏览轮廓，提取ROI并将其与相应的数字相关联
# loop over the OCR-A reference contours
for (i, c) in enumerate(refCnts):
    # compute the bounding box for the digit, extract it, and resize
    # it to a fixed size
    (x, y, w, h) = cv2.boundingRect(c)
    roi = ref[y:y + h, x:x + w]
    roi = cv2.resize(roi, (57, 88))
    cv2.imshow('roi', roi)
    cv2.waitKey(500)

    # update the digits dictionary, mapping the digit name to the ROI
    digits[i] = roi
# 从参考图像中提取数字，并将其与相应的数字名称相关联
print('digits:',digits.keys())
'''

# try1
digits = {}
rows, cols = ref.shape
per = int(cols / 10)
for x in range(10):
    roi = ref[:, x * per:(x + 1) * per]
    roi = cv2.resize(roi, (57, 88))
    cv2.imshow('roi', roi)
    cv2.waitKey(500)

    # update the digits dictionary, mapping the digit name to the ROI
    digits[x] = roi
# 从参考图像中提取数字，并将其与相应的数字名称相关联
print('digits:', digits.keys())

# 初始化一对结构化的内核：
# 您可以将内核看作是一个小矩阵，我们在图像上滑动以进行（卷积）操作，例如模糊，锐化，边缘检测或其他图像处理操作。
# initialize a rectangular (wider than it is tall) and square
# structuring kernel
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 读取信用卡相片
# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply a tophat (whitehat) morphological operator to find light
# regions against a dark background (i.e., the credit card numbers)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# compute the Scharr gradient of the tophat image, then scale
# the rest back into the range [0, 255]
gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0,
                  ksize=-1)
gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
gradX = gradX.astype("uint8")

# apply a closing operation using the rectangular kernel to help
# cloes gaps in between credit card number digits, then apply
# Otsu's thresholding method to binarize the image
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(gradX, 0, 255,
                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# apply a second closing operation to the binary image, again
# to help close gaps between credit card number regions
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)

# find contours in the thresholded image, then initialize the
# list of digit locations找到轮廓并初始化数字分组位置列表。
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
locs = []

# loop over the contours
for (i, c) in enumerate(cnts):
    # compute the bounding box of the contour, then use the
    # bounding box coordinates to derive the aspect ratio
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)

    # since credit cards used a fixed size fonts with 4 groups
    # of 4 digits, we can prune potential contours based on the
    # aspect ratio根据每个轮廓的宽高比进行过滤
    if ar > 2.5 and ar < 4.0:
        # contours can further be pruned on minimum/maximum width
        # and height使用纵横比，我们分析每个轮廓的形状。如果 ar   在2.5到4.0之间（比它高），以及  40到55个像素之间的 w以及   10到20像素之间的h，我们将一个方便的元组的边界矩形参数附加到 locs
        if (w > 40 and w < 55) and (h > 10 and h < 20):
            # append the bounding box region of the digits group
            # to our locations list
            locs.append((x, y, w, h))

# sort the digit locations from left-to-right, then initialize the
# list of classified digits
locs = sorted(locs, key=lambda x: x[0])
output = []

# loop over the 4 groupings of 4 digits
for (i, (gX, gY, gW, gH)) in enumerate(locs):
    # initialize the list of group digits
    groupOutput = []

    # extract the group ROI of 4 digits from the grayscale image,
    # then apply thresholding to segment the digits from the
    # background of the credit card
    group = gray[gY - 5:gY + gH + 5, gX - 5:gX + gW + 5]
    group = cv2.threshold(group, 0, 255,
                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # detect the contours of each individual digit in the group,
    # then sort the digit contours from left to right
    digitCnts = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('digitCnts', digitCnts[0])
    cv2.waitKey(1000)
    # digitCnts = digitCnts[0] if imutils.is_cv2() else digitCnts[1]
    digitCnts = digitCnts[1]
    # digitCnts = contours.sort_contours(digitCnts,method="left-to-right")[0]

    # loop over the digit contours
    for c in digitCnts:
        # compute the bounding box of the individual digit, extract
        # the digit, and resize it to have the same fixed size as
        # the reference OCR-A images
        (x, y, w, h) = cv2.boundingRect(c)
        roi = group[y:y + h, x:x + w]
        roi = cv2.resize(roi, (57, 88))

        # initialize a list of template matching scores
        scores = []

        # loop over the reference digit name and digit ROI
        for (digit, digitROI) in digits.items():
            # apply correlation-based template matching, take the
            # score, and update the scores list
            result = cv2.matchTemplate(roi, digitROI,
                                       cv2.TM_CCOEFF)
            (_, score, _, _) = cv2.minMaxLoc(result)
            scores.append(score)

        # the classification for the digit ROI will be the reference
        # digit name with the *largest* template matching score
        groupOutput.append(str(np.argmax(scores)))  # draw the digit classifications around the group
        cv2.rectangle(image, (gX - 5, gY - 5),
                      (gX + gW + 5, gY + gH + 5), (0, 0, 255), 2)
        cv2.putText(image, "".join(groupOutput), (gX, gY - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

    # update the output digits list
    output.extend(groupOutput)

# display the output credit card information to the screen
print("Credit Card Type: {}".format(FIRST_NUMBER.get(output[0], 'None')))
print("Credit Card #: {}".format("".join(output)))
cv2.imshow("Image", image)  # TODO 效果不是很好，需要改进
cv2.waitKey(0)
