# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)


# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

winname = 'example'
cv2.namedWindow(winname, 0)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
