#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: random 随机数
*
* Created by liuguoquan on 2017/10/23 16:40
*
"""

import random

# 0~1的小数
print(random.random())

# 输出a和b范围内的数，包括a和b
print(random.randint(1, 10))

# 输出start到stop-1之间的数，可设置步长
print(random.randrange(0, 4))
