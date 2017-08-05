#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 数字数据类型
*
* Created by liuguoquan on 2017/7/28 10:35
*
"""

import sys

# python3 默认编码
print(sys.getdefaultencoding())

# int型 可以存储到任意大小的整型
number = 9
print(type(number))  # int
# 查看内存地址
print(id(number))

number = int(9)
print(type(number))

# 负数
number = -178
print(number)

# float型
number = 9.9
print(type(number))  # float

# 布尔类型
number = True
print(type(number))  # bool
print(number == 1)  # True
print(number == 0)  # false

# 将字符转换为整数
number = int("99")
print(number)

number = float("99.99")
print(number)

# 将16进制转换为整数
number = int('0xf1', 16)
print(number)
number = int('100', 8)
number = int('10001', 2)

