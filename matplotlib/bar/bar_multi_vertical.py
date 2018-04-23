#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 垂直堆叠条形图
*
* Created by liuguoquan on 2018/4/3 11:23
*
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontManager, FontProperties


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


# 构建数据
Y2016 = [4000, 2000, 3000, 1000]
Y2017 = [4200, 3000, 2800, 1100]

railway = [20, 30, 22, 40, 55, 60, 45, 50]
road = [90, 30, 32, 40, 55, 60, 45, 50]
ship = [20, 30, 22, 40, 55, 60, 45, 50]
air = [20, 30, 22, 40, 55, 60, 45, 50]

s = list(map(lambda x: x[0] + x[1], zip(railway, road)))
s1 = list(map(lambda x: x[0] + x[1], zip(s, ship)))
s2 = list(map(lambda x: x[0] + x[1], zip(s1, air)))

xlabel = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月']

# 绘图
p1 = plt.bar(np.arange(8), railway, label='railway', width=0.4, align='center',
             color='green', alpha=0.8)
p2 = plt.bar(np.arange(8), road, bottom=railway, label='road', width=0.4, align='center', color='yellow', alpha=0.8)
p3 = plt.bar(np.arange(8), ship, bottom=s, label='ship', width=0.4, align='center', color='m',
             alpha=0.8)
p4 = plt.bar(np.arange(8), air, bottom=s1, label='air', width=0.4, align='center', color='blue', alpha=0.8)

# 添加轴标签
plt.xlabel('月份', fontproperties=getChineseFont())
plt.ylabel('货物量(万吨)', fontproperties=getChineseFont())

# 添加标题
plt.title('2017年各月份物流运输量', fontproperties=getChineseFont())
# 添加刻度标签
plt.xticks(np.arange(8), xlabel, fontproperties=getChineseFont())
# 设置y轴的刻度范围
plt.ylim([0, 280])

# 为每个条形图添加数值标签

# 显示图例
plt.legend(loc='upper center', ncol=4)

for x, y in enumerate(railway):
    plt.text(x - 0.2, y - 15, '%sW' % y)

for x, y in enumerate(s):
    plt.text(x - 0.2, y - 15, '%sW' % road[x])

for x, y in enumerate(s1):
    plt.text(x - 0.2, y - 15, '%sW' % ship[x])

for x, y in enumerate(s2):
    plt.text(x - 0.2, y - 15, '%sW' % air[x])

# 显示图形
plt.show()
