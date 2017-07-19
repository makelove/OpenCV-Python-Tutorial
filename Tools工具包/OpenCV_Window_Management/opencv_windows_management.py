# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 下午10:34
# @Author  : play4fun
# @File    : opencv_windows_management.py
# @Software: PyCharm

"""
opencv_windows_management.py:
"""

import cv2, math
import tkinter as tk


class Window:
    def __init__(self, name, image, weight=1):
        self.name = name
        self.image = image.copy()
        self.weight = weight
        self.shape = self.image.shape
        self.hight_x = self.shape[0]
        self.lenght_y = self.shape[1]


class opencv_windows_management:
    def __init__(self):
        self.windows = dict()

        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.screen_size = (screen_width, screen_height)  # (1280, 800)
        root.quit()

    def add(self, name, image, weight=1):
        '''
        权重,越高，图片显示越大
        :return:
        '''
        cv2.namedWindow(name, flags=cv2.WINDOW_AUTOSIZE)
        window = Window(name, image, weight)
        self.windows[name] = window
        # self.windows[name] = image

    def show(self):
        lenw = len(self.windows)
        w_l = int(self.screen_size[0] / lenw)

        max_num_line = math.ceil(math.sqrt(lenw))  # 取平方根
        # TODO 权重

        for i, name in enumerate(self.windows):
            # if (i+1) >max_num_line:
            #     #TODO 换行
            #     cv2.moveWindow(name, w_l * i, h_x*j)
            #     pass

            win = self.windows[name]
            image = win.image
            # image = self.windows[name]
            # h_x = int(image.shape[1] / w_l * image.shape[0]) #保持比例
            h_x = int(w_l / win.lenght_y * win.hight_x)  # 保持比例
            # print((w_l,h_x))
            img2 = cv2.resize(image, (w_l, h_x))
            cv2.moveWindow(name, w_l * i, 0)
            cv2.imshow(name, img2)
