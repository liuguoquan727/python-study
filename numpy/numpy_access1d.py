#!/usr/bin/env python
# coding=utf-8

"""
*
* 存取元素
* Created by Michael on 2017/3/2 16:59.
*
"""

import numpy as np

__author__ = 'Michael'

a = np.arange(10)
print(a)

print("获取数组中的元素")
print(a[5])
print()

print("切片获取一部分元素")
print(a[3:5])
print(a[:5])
print(a[:-1])
print(a[:])
# 步长为2取出元素
print(a[0:-1:2])
# 逆序访问数组元素
print(a[::-1])
print()

print("改变数组中的元素")
a[5] = 10
print(a)
# 下标修改元素的值
a[2:4] = 12, 14
print(a)
print()

print("通过切片产生一个新的数组")
b = a[3:6]
print(b)
# b和a共享同一块数据空间
b[0] = 99
print(a)
print()

x = np.arange(0, 10)
print(x)
# 获取数组x下表为1，2，3，4的元素组成一个新的数组
y = x[[1, 2, 3, 4]]
print(y)
# x和y不共享数据空间
y[0] = 10
print(x)
print()

print("布尔比较")
# 生成10个0~1的随机数
x = np.random.rand(10)
print(x)
print(x > 0.5)
print(x[x > 0.5])
print()
