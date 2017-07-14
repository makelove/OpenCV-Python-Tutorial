# -*- coding: utf-8 -*-

'''
以 Haar 特征分类器为基础的面部检测技术
将面部检测扩展到眼部检测等。

以 Haar 特征分类器为基础的对 检测技术是一种 常有效的对 检测 技术 2001 年 Paul_Viola 和 Michael_Jones 提出 。它是基于机器学习的    使用大 的正 样本图像 练得到一个 cascade_function 最后再用它 来做对 检测。
现在我们来学习  检测。开始时 算法  大 的正样本图像   图 像 和 样本图像 不含  的图像 来 练分类器。我们  从其中提取特 征。下图中的 Haar 特征会 使用。它们就像我们的卷积核。每一个特征是一 个值  个值等于 色矩形中的像素值之后减去白色矩形中的像素值之和。

 那么我们怎样从超过160000+ 个特征中 出最好的特征呢 ？
 使用 Adaboost。

OpenCV 自带了训练器和检测器。如果你想自己训练一个分类器来检测 汽车飞机等的
可以使用 OpenCV 构建。
Cascade Classifier Training :http://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html


'''

import numpy as np
import cv2

# 运行之前，检查cascade文件路径是否在你的电脑上
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

# img = cv2.imread('../data/sachin.jpg')
# img = cv2.imread('../data/kongjie_hezhao.jpg')
img = cv2.imread('../data/airline-stewardess-bikini.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)


# Detects objects of different sizes in the input image.
# The detected objects are returned as a list of rectangles.
# cv2.CascadeClassifier.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
# scaleFactor – Parameter specifying how much the image size is reduced at each image
# scale.
# minNeighbors – Parameter specifying how many neighbors each candidate rectangle should
# have to retain it.
# minSize – Minimum possible object size. Objects smaller than that are ignored.
# maxSize – Maximum possible object size. Objects larger than that are ignored.
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print("Detected ", len(faces), " face")

for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
