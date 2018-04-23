#!/usr/bin/env python3
# coding=utf-8

"""
*
* 多维数组
* Created by Michael on 2017/3/6 15:52.
*
"""

import numpy as np

__author__ = 'Michael'

"""
* numpy采用元组作为数组的下标，元组中的每个元素与数组中的每个轴对应
"""

a = np.arange(0, 60, 10)
print(a)

# -1表示自动计算该轴的长度
a = a.reshape(-1, 1)
print(a)
b = np.arange(0, 6)
print(b)

# 相加
print("相加")
a = a + b
print(a)
print("\n")

# 相当于打印(0,3) (0,5)数据
print(a[0, 3:5])
print(a)

# 相当于打印(4,4) (4,5) (5,4) (5,5)数据
print(a[4:, 4:])

# 相当于打印序号为2列数据
print(a[:, 2])

# a b共享数据空间
b = a[0, 3:5]
print(b)
b[0] = -b[0]
print(a)
