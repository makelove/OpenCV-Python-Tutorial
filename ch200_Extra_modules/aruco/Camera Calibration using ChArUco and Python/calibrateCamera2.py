# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 18:04
# @Author  : play4fun
# @File    : calibrateCamera2.py
# @Software: PyCharm

"""
calibrateCamera2.py:
"""

import cv2
import numpy as np


def draw_axis(img, charuco_corners, charuco_ids, board):
    vecs = np.load("./calib.npz")  # I already calibrated the camera
    mtx, dist, _, _ = [vecs[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]
    ret, rvec, tvec = cv2.aruco.estimatePoseCharucoBoard(
        charuco_corners, charuco_ids, board, mtx, dist)
    if ret is not None and ret is True:
        cv2.aruco.drawAxis(img, mtx, dist, rvec, tvec, 0.1)


def get_image(camera):
    ret, img = camera.read()
    return img


def make_grayscale(img):
    ret = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return ret


def main():
    camera = cv2.VideoCapture(0)
    img = get_image(camera)
    while True:
        cv2.imshow('calibration', img)
        cv2.waitKey(10)
        img = get_image(camera)
        gray = make_grayscale(img)
        corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict,
                                                         corners, ids)
        cv2.aruco.drawDetectedMarkers(img, corners, ids)
        if ids is not None and corners is not None \
                and len(ids) > 0 and len(ids) == len(corners):
            diamond_corners, diamond_ids = \
                cv2.aruco.detectCharucoDiamond(img, corners, ids,
                                               0.05 / 0.03, cameraMatrix=mtx,
                                               distCoeffs=dist)
            cv2.aruco.drawDetectedDiamonds(img, diamond_corners, diamond_ids)
            '''if diamond_ids is not None and len(diamond_ids) >= 4:
                break'''
            board = cv2.aruco.CharucoBoard_create(9, 6, 0.05, 0.03,
                                                  aruco_dict)
            if diamond_corners is not None and diamond_ids is not None \
                    and len(diamond_corners) == len(diamond_ids):
                count, char_corners, char_ids = \
                    cv2.aruco.interpolateCornersCharuco(diamond_corners,
                                                        diamond_ids, gray,
                                                        board)
                if count >= 3:
                    draw_axis(img, char_corners, char_ids, board)


if __name__ == '__main__':
    main()
