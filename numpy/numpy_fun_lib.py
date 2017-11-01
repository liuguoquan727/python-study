#!/usr/bin/env python
# coding=utf-8

"""
*
*
* Created by Michael on 2017/3/14 15:42.
*
"""

import numpy as np

__author__ = 'Michael'

"""
求和
"""

a = np.random.randint(0, 10, size=(5, 5))
print(a)

ret = np.sum(a)
print(ret)
# 按行求和
ret = np.sum(a, axis=1)
print(ret)
# 按列求和
ret = np.sum(a, axis=0)
print(ret)

"""
求平均值
"""
ret = np.mean(a)
print(ret)
ret = np.mean(a, axis=1)
print(ret)
ret = np.mean(a, axis=0)
print(ret)

"""
标准差
"""
ret = np.std(a, axis=1)
print(ret)

"""
方差
"""
ret = np.var(a, axis=1)
print(ret)

"""
最值
"""

# 最大值
ret = np.max(a)
print(ret)

# 最小值
ret = np.min(a)
print(ret)

# 最大值与最小值的差值
ret = np.ptp(a)
print(ret)

# 第一个最大值的下标
ret = np.argmax(a)
print(ret)
# 每行的最大值的下标
ret = np.argmax(a, axis=1)
print(ret)

# 第一个最小值的下标
ret = np.argmin(a)
print(ret)

"""
排序
"""

# 对每行数据进行排序
ret = np.sort(a)
print(ret)

# 对每列数据进行排序
ret = np.sort(a, axis=0)
print(ret)

# 数组的排序下标
ret = np.argsort(a)
print(ret)

# 获取排序后的中值，当长度是偶数时,得到中间两个数的平均值
ret = np.median(a)
print(ret)
