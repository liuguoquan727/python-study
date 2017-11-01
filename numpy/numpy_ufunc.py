#!/usr/bin/env python
# coding=utf-8

"""
*
* ufunc运算 universal function 能对数组中每个元素进行操作的函数
* Created by Michael on 2017/3/6 16:34.
*
"""

import numpy as np

__author__ = 'Michael'

# sin
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
print(y)

# 结果保存在x中
t = np.sin(x, out=x)
print(x)
print(id(x) == id(t))

"""
*
* 四则运算
*
"""

a = np.arange(0, 4)
print(a)
b = np.arange(1, 5)
print(b)

# a + b
ret = np.add(a, b)
print(ret)

# np.add(a, b, a) // a += b

# b - a
ret = np.subtract(b, a)
print(ret)

# a * b
ret = np.multiply(a, b)
print(ret)

# a^b
ret = np.power(a, b)
print(ret)

# a / b
ret = np.divide(a, b)
print(ret)
# 返回精确的值
ret = np.true_divide(a, b)
print(ret)
# 取整
ret = np.floor_divide(a, b)
print(ret)

# y = -x
ret = np.negative(a)
print(ret)

# a % b 模除
ret = np.remainder(a, b)
print(ret)

"""
*
* 比较和布尔运算
*
"""

# a == b
ret = np.equal(a, b)
print(ret)

# a != b
ret = np.not_equal(a, b)
print(ret)

# a < b
ret = np.less(a, b)
print(ret)

# a <= b
ret = np.less_equal(a, b)
print(ret)

# a > b
ret = np.greater(a, b)
print(ret)

# a >= b
ret = np.greater_equal(a, b)
print(ret)

# a or b
ret = np.logical_or(a, b)
print(ret)

# a and b
ret = np.logical_and(a, b)
print(ret)

# a not b 取反
ret = np.logical_not(a)
print(ret)

#
# a xor b 异或
ret = np.logical_xor(a, b)
print(ret)
