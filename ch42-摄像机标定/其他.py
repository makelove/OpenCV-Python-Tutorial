# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午6:29
# @Author  : play4fun
# @File    : 其他.py
# @Software: PyCharm

"""
其他.py:
"""
import cv2

# 标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 畸变校正
img = cv2.imread('left12.jpg')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# 使用 cv2.undistort()  是最简单的方法。只 使用这个函数和上面得到 的 ROI 对结果进行裁剪。

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv2.imwrite('calibresult.png', dst)

# 使用 remapping  应 属于 曲线救国 了。 先我们 找到从畸变图像到畸变图像的映射方程。再使用 重映射方程
# undistort
mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
# crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv2.imwrite('calibresult.png', dst)
# 你会发现结果图像中所有的边界 变直了

# 反向投影误差
# 我们可以利用反向投影 差对我们找到的参数的准确性  估 。
# 得到的 结果越接近 0 越好。有了内部参数 畸变参数和旋 变换矩  我们就可以使 用 cv2.projectPoints() 将对象点转换到图像点。
# 然后就可以 算变换得到 图像与角点检测算法的绝对差了。
# 然后我们计算所有标定图像的误差平均值。
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error
print("total error: ", mean_error / len(objpoints))
