#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: series的使用
*
* Created by liuguoquan on 2017/12/15 19:37
*
"""

import numpy as np
import pandas as pd

# 1. 通过一维数组创建序列

arr1 = np.arange(10)
print(type(arr1))
print(arr1)

s1 = pd.Series(arr1)
print(type(s1))
print(s1)

# 2. 通过字典的方式创建序列

dict1 = {"a": 10, "b": 20, "c": 30}
print(dict1)

s2 = pd.Series(dict1)
print(type(s2))
print(s2)

"""
序列的索引
"""

print(s2[0])  # 取第一个元素
print(s2[1:3])  # 取 2，3个元素
print(s2[::2])  # 依次取元素，步长为2

"""
iat 方法 倒数的方式取元素
"""

print(s2.iat[-1])  # 取倒数第一个元素
print(s2[-1])

"""
布尔索引
"""

np.random.seed(23)
s4 = pd.Series(np.random.randint(size=5, low=1, high=100))
print(s4)
print(s4[s4 > 50])  # 大于50的值
print(s4[s4 > 20][s4 < 60])  # 大于20 小于60的值
