#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: DataFrame 数据框
*
* Created by liuguoquan on 2017/12/15 19:45
*
"""

import numpy as np
import pandas as pd

# 1. 通过二位数组创建数据框

arr = np.arange(10).reshape(5, 2)
pd0 = pd.DataFrame(arr, columns=["V1", "V2"])
print(pd0)

# 2. 通过字典的方式创建数据框

# 字典列表
dict1 = {"a": [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
print(dict1)

pd1 = pd.DataFrame(dict1)
print(pd1)
print(type(pd1))

# 嵌套字典
dict2 = {"one": {"a": 10, "b": 20, "c": 30}, 'two': {"a": 10, "b": 20, "c": 30}, 'three': {"a": 10, "b": 20, "c": 30}}
pd2 = pd.DataFrame(dict2)
print(pd2)
print(type(pd2))

# 3. 通过数据框的方式创建数据框

pd3 = pd2[['one', 'two']]
print(pd3)

# 选择数据框中的某一列，返回一个序列的对象
pd4 = pd2['one']
print(pd4)

print(pd2.shape)
print(pd2.columns)
print(pd2.describe())
