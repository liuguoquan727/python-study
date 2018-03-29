#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 读取cvs数据
*
* Created by liuguoquan on 2018/2/8 15:56
*
"""

import pandas as pd

ss = pd.read_csv("./ticket_3_80.csv")

# 取出数据
# print(ss)
print(ss.head(n=10))

# 名称索引法取出列数据
print(ss["id"].head())

# 点取法取出列数据
print(ss.id.head())

# 数据筛选
# num = 80 的数据项
print(ss.loc[ss.num == 80].head())

# num >= 80 num < 90
print(ss.loc[(ss.num >= 80) & (ss.num < 90)].head())
