#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 方框滤波
*
* Created by liuguoquan on 2017/10/11 16:47
*
"""

import cv2

src = cv2.imread("../lena.png")

cv2.imshow("src", src)

dst = cv2.boxFilter(src, -1, (5, 5))

cv2.imshow("dst", dst)

cv2.waitKey(0)

