#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 双边滤波
*
* Created by liuguoquan on 2017/10/13 14:08
*
"""


import cv2

src = cv2.imread("../lena.png")

cv2.imshow("src", src)

dst = cv2.bilateralFilter(src, 25, 25 * 2, 25 / 2)

cv2.imshow("bilateral dst", dst)

cv2.waitKey(0)

