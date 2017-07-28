# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 15:38
# @Author  : play4fun
# @File    : aruco11.py
# @Software: PyCharm

"""
aruco11.py:
"""

import time, cv2
# import cv2.aruco as A
import numpy as np

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
board = cv2.aruco.CharucoBoard_create(9, 9, .025, .0125, dictionary)
img = board.draw((200 * 9, 200 * 9))
# cv2.imshow('board',img)
# cv2.waitKey(0)

# Dump the calibration board to a file
# cv2.imwrite('charuco.png', img)
#用打印机打印出来

# Start capturing images for calibration
cap = cv2.VideoCapture(0)

allCorners = []
allIds = []
decimator = 0
for i in range(200):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.aruco.detectMarkers(gray, dictionary)

    if len(res[0]) > 0:
        print('len(res[0]):',len(res[0]))

        res2 = cv2.aruco.interpolateCornersCharuco(res[0], res[1], gray, board)
        if res2[1] is not None and res2[2] is not None and len(res2[1]) > 3 and decimator % 3 == 0:
            allCorners.append(res2[1])
            allIds.append(res2[2])

        cv2.aruco.drawDetectedMarkers(gray, res[0], res[1])

    cv2.imshow('frame', gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    decimator += 1

imsize = gray.shape

# Calibration fails for lots of reasons. Release the video if we do
try:
    cal = cv2.aruco.calibrateCameraCharuco(allCorners, allIds, board, imsize, None, None)#return retval, cameraMatrix, distCoeffs, rvecs, tvecs
    print(cal)
    retval, cameraMatrix, distCoeffs, rvecs, tvecs = cal#TODO 然后怎么办？
    #TODO saveCameraParams
    np.savez('calib.npz',mtx=cameraMatrix,dist=distCoeffs,rvecs=rvecs,tvecs=tvecs)#保存下载，下次不用校准了。
    # np.savez(outfile, x=x, y=y)
except:
    cap.release()

cap.release()
cv2.destroyAllWindows()


'''
retval, cameraMatrix, distCoeffs, rvecs, tvecs

(40.66987516955983, array([[  1.51699257e+03,   0.00000000e+00,   8.53629301e+02],
       [  0.00000000e+00,   4.50213990e+02,   7.76441549e+02],
       [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]]), array([[-0.11643503, -0.05270646, -0.02284758,  0.00088231,  0.01165172]]), [array([[ 0.6077912 ],
       [-1.42834429],
       [ 0.30243197]]), array([[ 0.6201644 ],
       [-1.43661477],
       [ 0.27205568]]), array([[ 0.62042201],
       [-1.42419143],
       [ 0.30919894]]), array([[ 0.6249636 ],
       [-1.42055174],
       [ 0.31823623]]), array([[ 0.51973251],
       [-1.46121409],
       [ 0.15266338]]), array([[ 0.62205772],
       [-1.42727173],
       [ 0.31075834]]), array([[ 2.02157844],
       [-1.75270325],
       [ 0.40542169]]), array([[ 2.01139176],
       [-1.75092153],
       [ 0.39164267]]), array([[ 2.02392487],
       [-1.74645837],
       [ 0.40174685]]), array([[ 2.01210339],
       [-1.74882078],
       [ 0.39050991]]), array([[ 0.87226228],
       [-1.50949168],
       [ 0.44230903]]), array([[ 0.87536626],
       [-1.51319442],
       [ 0.44075465]]), array([[ 0.88520206],
       [-1.52335331],
       [ 0.37352831]]), array([[ 0.07658779],
       [ 0.58155207],
       [ 1.24758432]])], [array([[ 0.10636704],
       [-0.25196328],
       [ 0.14970101]]), array([[ 0.10401605],
       [-0.24774933],
       [ 0.13947949]]), array([[ 0.10785286],
       [-0.24809633],
       [ 0.1447296 ]]), array([[ 0.10974635],
       [-0.25258058],
       [ 0.1578239 ]]), array([[ 0.07912493],
       [-0.24214649],
       [ 0.09198621]]), array([[ 0.10862882],
       [-0.24818928],
       [ 0.14389561]]), array([[ 0.1889342 ],
       [-0.4414372 ],
       [ 0.18697331]]), array([[ 0.18888891],
       [-0.44753235],
       [ 0.18719762]]), array([[ 0.18888745],
       [-0.45388025],
       [ 0.192372  ]]), array([[ 0.18836521],
       [-0.43764759],
       [ 0.18195927]]), array([[ 0.09873032],
       [-0.44646521],
       [ 0.09927093]]), array([[ 0.0997728 ],
       [-0.43749325],
       [ 0.09494866]]), array([[ 0.09320065],
       [-0.44113935],
       [ 0.08896787]]), array([[ 0.10408231],
       [-0.5532671 ],
       [ 0.17006767]])])
'''