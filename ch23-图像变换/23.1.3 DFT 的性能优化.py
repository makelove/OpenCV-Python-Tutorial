# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 上午11:12
# @Author  : play4fun
# @File    : 23.1.3 DFT 的性能优化.py
# @Software: PyCharm

"""
23.1.3 DFT 的性能优化.py:
"""
import numpy as np

# In [16]: img = cv2.imread('messi5.jpg',0)
# In [17]: rows,cols = img.shape
# In [18]: print rows,cols
# 342 548
# In [19]: nrows = cv2.getOptimalDFTSize(rows)
# In [20]: ncols = cv2.getOptimalDFTSize(cols)
# In [21]: print nrows, ncols
# 360 57

nimg = np.zeros((nrows,ncols))
nimg[:rows,:cols] = img

#或者
right = ncols - cols
bottom = nrows - rows
#just to avoid line breakup in PDF file
bordertype = cv2.BORDER_CONSTANT
nimg = cv2.copyMakeBorder(img,0,bottom,0,right,bordertype, value = 0)

#现在我们看看 Numpy 的 现

In [22]: %timeit fft1 = np.fft.fft2(img)
10 loops, best of 3: 40.9 ms per loop
In [23]: %timeit fft2 = np.fft.fft2(img,[nrows,ncols])
100 loops, best of 3: 10.4 ms per loop

# 度提 了 4 倍。我们再看看 OpenCV 的 现
In [24]: %timeit dft1= cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
100 loops, best of 3: 13.5 ms per loop

In [27]: %timeit dft2= cv2.dft(np.float32(nimg),flags=cv2.DFT_COMPLEX_OUTPUT)
100 loops, best of 3: 3.11 ms per loop
