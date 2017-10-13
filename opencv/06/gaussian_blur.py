#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 高斯滤波
*
* Created by liuguoquan on 2017/10/11 16:47
*
"""

import cv2

src = cv2.imread("../lena.png")

cv2.imshow("src", src)

dst = cv2.GaussianBlur(src, (5, 5), 0)

cv2.imshow("gaussian dst", dst)

cv2.waitKey(0)

