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

"""
序列去重及水平统计
"""

np.random.seed(10)
s = np.random.randint(size=1000, low=1, high=4)

# 去重
print(pd.unique(s))

# 水平统计 计数
print(pd.value_counts(s))

"""
序列的排序
"""

np.random.seed(1)
s = pd.Series(np.random.normal(size=4))

# 按索引升序排序
print(s.sort_index(ascending=True))

# 按索引降序排序
print(s.sort_index(ascending=False))

# 按序列的值升序排序
print(s.sort_values())

"""
抽样 sample 函数

s.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)

n：指定抽取的样本量；
frac：指定抽取的样本比例；
replace：是否有放回抽样，默认无放回；
weights：指定样本抽中的概率，默认等概论抽样；
random_state：指定抽样的随机种子；
"""
print("抽样sample函数")
s = pd.Series(range(1, 101))
print(s.sample(n=3, random_state=2))

s = pd.Series(range(1, 6))
print(s.sample(n=3, replace=True, random_state=2))

s = pd.Series(['男', '女'])
print(s.sample(n=10, replace=True, weights=[0.2, 0.8], random_state=2))

"""
统计运算
"""

"""
describe函数 统计值汇总函数

count    100.000000
mean      14.870000
std        7.973004
min        0.000000
25%        9.000000
50%       15.000000
75%       21.250000
max       29.000000
"""

np.random.seed(1234)
s = pd.Series(np.random.randint(size=100, low=0, high=30))
print(s.describe())

s = pd.Series([1, 2, np.nan, 4, np.nan, 6])
print(s)
print(s.isnull())

# 常用的统计函数

"""
s.min()  # 最小值
s.quantile(q=[0,0.25,0.5,0.75,1]) # 分位数函数
s.median()  # 中位数
s.mode()  # 众数
s.mean()  # 平均值
s.mad()  # 平均绝对误差
s.max  # 最大值
s.sum()  # 和
s.std()  # 标准差
s.var()  # 方差
s.skew()  # 偏度
s.kurtosis()  # 峰度
s.cumsum()  # 和的累计，返回序列
s.cumprod()  # 乘积的累积，返回序列
s.product()  # 序列元素乘积
s.diff()  # 序列差异（微分），返回序列
s.abs()  # 绝对值，返回序列
s.pct_change()  # 百分比变化 ，返回序列
s.corr(s2)  # 相关系数
s.ptp()  # 极差  R中的range函数
"""
