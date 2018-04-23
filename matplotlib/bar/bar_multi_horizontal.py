#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 水平交错条形图
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

xlabel = ['北京', '上海', '广州', '深圳']

# 绘图
p1 = plt.bar(np.arange(4), Y2016, label='2016', width=0.4, align='center', color='red', alpha=0.8)
p2 = plt.bar(np.arange(4) + 0.4, Y2017, label='2017', width=0.4, align='center', color='green', alpha=0.8)

# 添加轴标签
plt.xlabel('Top4城市', fontproperties=getChineseFont())
plt.ylabel('家庭数量', fontproperties=getChineseFont())

# 添加标题
plt.title('亿万财富家庭Top4城市分布', fontproperties=getChineseFont())
# 添加刻度标签
plt.xticks(np.arange(4) + 0.2, xlabel, fontproperties=getChineseFont())
# 设置y轴的刻度范围
plt.ylim([0, 5000])

# 为每个条形图添加数值标签
for x, y in enumerate(Y2016):
    plt.text(x - 0.2, y + 100, '%s' % y)

for x, y in enumerate(Y2017):
    plt.text(x + 0.2, y + 100, '%s' % y)

# 显示图例
plt.legend()

# 显示图形
plt.show()
