#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 中值滤波
*
* Created by liuguoquan on 2017/10/13 14:08
*
"""


import cv2

src = cv2.imread("../lena.png")

cv2.imshow("src", src)

dst = cv2.medianBlur(src, 5)

cv2.imshow("median blur dst", dst)

cv2.waitKey(0)

