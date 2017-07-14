# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午11:43
# @Author  : play4fun
# @File    : HDR.py
# @Software: PyCharm

"""
HDR.py:
http://docs.opencv.org/3.2.0/d2/df0/tutorial_py_hdr.html

了解如何从曝光序列生成和显示HDR图像。
使用曝光融合合并曝光序列。

高动态范围成像（HDRI或HDR）是一种用于成像和摄影的技术，可以重现比标准数字成像或摄影技术更大的动态光度范围。虽然人眼可以调整到广泛的光线条件，但大多数成像设备每通道使用8位，因此我们仅限于256级。当我们拍摄现实世界的场景时，明亮的地区可能曝光过度，而黑暗的区域可能曝光不足，所以我们无法使用单次曝光拍摄所有细节。HDR图像与每个通道使用超过8位（通常为32位浮点值）的图像一起使用，允许更宽的动态范围。

有不同的获取HDR图像的方法，但最常见的是使用不同曝光值拍摄的场景的照片。要组合这些曝光，了解您的相机的响应功能是有用的，并且有算法来估计它。合并HDR图像后，必须将其转换回8位才能在通常的显示屏上进行查看。这个过程叫做tonemapping。当场景或相机的对象在拍摄之间移动时，会出现附加的复杂性，因为具有不同曝光的图像应该被注册和对齐。

在本教程中，我们展示了两种算法（Debvec，Robertson）从曝光序列生成和显示HDR图像，并展示了一种称为曝光融合（Mertens）的替代方法，它产生低动态范围图像，不需要曝光时间数据。此外，我们估计对于许多计算机视觉算法具有重要价值的相机响应函数（CRF）。HDR管道的每一步都可以使用不同的算法和参数来实现，因此请参考参考手册来查看。



"""

import cv2
import numpy as np

# 第一阶段只是将所有图像加载到列表中。此外，我们将需要常规HDR算法的曝光时间。注意数据类型，因为图像应为1通道或3通道8位（np.uint8），曝光时间需要为float32，以秒为单位。
# Loading exposure images into a list
img_fn = ["1tl.jpg", "2tr.jpg", "3bl.jpg", "4br.jpg"]
img_list = [cv2.imread(fn) for fn in img_fn]
exposure_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)

# Merge exposures to HDR image
# 在这个阶段，我们将曝光序列合并成一个HDR图像，显示了我们在OpenCV中的两种可能性。第一种方法是Debvec，第二种是Robertson。请注意，HDR图像的类型为float32，而不是uint8，因为它包含所有曝光图像的完整动态范围。

merge_debvec = cv2.createMergeDebevec()
hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy())
merge_robertson = cv2.createMergeRobertson()
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy())

# Tonemap HDR image
# 我们将32位浮点HDR数据映射到范围[0..1]。实际上，在某些情况下，值可能大于1或低于0，所以注意我们以后不得不剪切数据，以避免溢出。
tonemap1 = cv2.createTonemapDurand(gamma=2.2)
res_debvec = tonemap1.process(hdr_debvec.copy())
tonemap2 = cv2.createTonemapDurand(gamma=1.3)
res_robertson = tonemap2.process(hdr_robertson.copy())

# Exposure fusion using Mertens
# 这里我们展示了一种可以合并曝光图像的替代算法，我们不需要曝光时间。我们也不需要使用任何tonemap算法，因为Mertens算法已经给出了[0..1]范围内的结果。
merge_mertens = cv2.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

# Convert datatype to 8-bit and save
# 为了保存或显示结果，我们需要将数据转换为[0..255]范围内的8位整数。
res_debvec_8bit = np.clip(res_debvec * 255, 0, 255).astype('uint8')
res_robertson_8bit = np.clip(res_robertson * 255, 0, 255).astype('uint8')
res_mertens_8bit = np.clip(res_mertens * 255, 0, 255).astype('uint8')

cv2.imwrite("ldr_debvec.jpg", res_debvec_8bit)
cv2.imwrite("ldr_robertson.jpg", res_robertson_8bit)
cv2.imwrite("fusion_mertens.jpg", res_mertens_8bit)

exit(0)

# Estimate camera response function (CRF)
# 相机响应功能（CRF）给出了场景辐射度与测量强度值之间的连接。如果在一些计算机视觉算法中非常重要，包括HDR算法，CRF。这里我们估计反相机响应函数并将其用于HDR合并。
cal_debvec = cv2.createCalibrateDebevec()
crf_debvec = cal_debvec.process(img_list, times=exposure_times)
hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy(), response=crf_debvec.copy())
cal_robertson = cv2.createCalibrateRobertson()
crf_robertson = cal_robertson.process(img_list, times=exposure_times)
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy(), response=crf_robertson.copy())
