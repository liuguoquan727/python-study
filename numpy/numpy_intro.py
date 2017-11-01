#!/usr/bin/env python
# coding=utf-8

"""
*
* numpy基本使用
* Created by Michael on 2017/3/1 17:16.
*
"""

import numpy as np

__author__ = 'Michael'

print("创建数组")
a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print()

print(a)
print(b)
print(c)
print()
print("获取数组的形状：是一个描述数组各个轴的元组")
print(a.shape)
print(c.shape)
print()

print("创建指定形状的新数组 原数组a保持不变")
d = a.reshape(4)
print(d)
print()

print("a和d共享内存空间 a改变时d也会改变")
a[1] = 100
print(d)

print()
print("数组元素类型")
print(d.dtype)

print()
print("完整类型列表")
print(set(np.typeDict.values()))
print()

print("0~1 步长为1/10 的等差数组")
arrange = np.arange(0, 1, 0.1)
print(arrange)
print()

print("包含终值 1~100 步长为1/9等差数列")
space = np.linspace(0, 100, 10)
print(space)
print()

print("不包含终值 步长为1/10等差数列")
space = np.linspace(0, 100, 10, endpoint=False)
print(space)
print()

print("创建 10^0 ~ 10^2 有5个元素的等比数列")
logspace = np.logspace(0, 2, 5)
print(logspace)
print()

print("创建 一个比列为2^(1/12)的等比数列 2^0 ~ 2^1")
logspace = np.logspace(0, 2, 12, base=2, endpoint=True)
print(logspace)
print()

print("创建指定的数组,不对其进行初始化")
empty = np.empty((2, 3), np.int64)
print(empty)
print()

print("创建指定的数组,初始化为0")
zero = np.zeros((2, 3), np.int64)
print(zero)
print()

print("创建指定的数组,初始化为1")
one = np.ones((2, 3), np.int64)
print(one)
print()

print("从字符序列创建数组")
s = "abcdefg"
array = np.fromstring(s, dtype=np.int8)
print(array)
print()

print("从函数值创建数组 99乘法表")


def func1(i, j):
    return (i + 1) * (j + 1)


a = np.fromfunction(func1, (9, 9))
print(a)
print()
