#!/usr/bin/env python
# coding=utf-8

"""
*
* 结构数组
* Created by Michael on 2017/3/6 16:15.
*
"""

import numpy as np

__author__ = 'Michael'

persontype = np.dtype({'names': ['name', 'age', 'weight'], 'formats': ['S32', 'i', "l"]}, align=True)

a = np.array([("Zhang", 32, 75), ("Lau", 26, 65)], dtype=persontype)

print(a.dtype)
print(a)
print(a[0]["name"])
a[0]["name"] = "lee"
print(a[0]["name"])

# a中所有age字段的值的数组
b = a["age"]
print(b)
