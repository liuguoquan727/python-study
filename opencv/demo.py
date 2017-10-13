#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2017/10/11 16:34
*
"""

import cv2

image = cv2.imread('lena.png')
cv2.namedWindow("Image")
cv2.moveWindow("Image", 100, 100)
cv2.imshow("Image", image)
cv2.imshow("11",image)
cv2.waitKey(0)

