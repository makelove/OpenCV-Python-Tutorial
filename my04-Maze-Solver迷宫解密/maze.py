

'''
源文件是使用opencv2.4，
改成opencv3.2有点问题。
https://ishankgulati.github.io/posts/Maze-Solver/
'''
import cv2
import numpy as np



img = cv2.imread('SampleImages/1.png')
# img = cv2.imread('SampleImages/2.png')
# img = cv2.imread('SampleImages/3.jpg')#不行，得修改
# img = cv2.imread('SampleImages/huge_maze.jpg')#不行，得修改
cv2.imshow('maze',img)
cv2.waitKey(0)

# Binary conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)#反转tholdolding将给我们一个二进制的图像与白色的墙壁和黑色的背景。
cv2.imshow('THRESH_BINARY_INV',thresh)
cv2.waitKey(0)

# Contours
image,contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
print('len(contours):',len(contours))
# dc=cv2.drawContours(thresh, contours, 0, (255, 255, 255), -1)
dc=cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)#用不同颜色来标注
dc=cv2.drawContours(dc, contours, 1, (0, 0, 0), 5)# TODO 大迷宫的len(contours): 26
cv2.imshow('drawContours',dc)
cv2.waitKey(0)

ret, thresh = cv2.threshold(dc, 240, 255, cv2.THRESH_BINARY)
# ret, thresh = cv2.threshold(thresh, 240, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh2',thresh)
cv2.waitKey(0)

# Dilate
'''
扩张

扩张是数学形态领域的两个基本操作者之一，另一个是侵蚀。它通常应用于二进制图像，但有一些版本可用于灰度图像。操作者对二进制图像的基本效果是逐渐扩大前景像素区域的边界（通常为白色像素）。因此，前景像素的面积大小增加，而这些区域内的孔变小。
'''
ke = 10
# kernel = np.ones((19, 19), np.uint8)
kernel = np.ones((ke, ke), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)

# Erosion
#侵蚀是第二个形态运算符。它也适用于二进制图像。操作者对二进制图像的基本效果是消除前景像素区域的边界（通常为白色像素）。因此，前景像素的面积缩小，并且这些区域内的孔变大。
erosion = cv2.erode(dilation, kernel, iterations=1)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)

#找到两个图像的差异
diff = cv2.absdiff(dilation, erosion)
cv2.imshow('diff',diff)
cv2.waitKey(0)

# splitting the channels of maze
b, g, r = cv2.split(img)
mask_inv = cv2.bitwise_not(diff)
#为了在原始迷宫图像上显示解决方案，首先将原来的迷宫分割成r，g，b组件。现在通过反转diff图像创建一个掩码。使用在最后一步中创建的掩码的原始迷宫的按位和r和g分量。这一步将从迷宫解决方案的图像部分去除红色和绿色成分。最后一个是合并所有组件，我们将使用蓝色标记的解决方案。
# masking out the green and red colour from the solved path
r = cv2.bitwise_and(r, r, mask=mask_inv)
g = cv2.bitwise_and(g, g, mask=mask_inv)

res = cv2.merge((b, g, r))
cv2.imshow('Solved Maze', res)
cv2.imwrite('SampleImages/Solved-Maze-1.png',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
