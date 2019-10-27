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

ss = pd.read_csv("./tancan_1.csv")

# 取出数据
print(ss)

# 名称索引法取出列数据
# print(ss["full"].head())

# # 点取法取出列数据
# print(ss.id.head())
