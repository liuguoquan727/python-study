#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 垂直条形图
*
* Created by liuguoquan on 2018/4/3 11:23
*
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager, FontProperties


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


GDP = [12000, 800, 9000, 20000]

# 构建数据
GDP = [12406.8, 13908.57, 9386.87, 9143.64]

# 绘图
plt.bar(range(4), GDP, align='center', color='red', alpha=0.8)
# 添加轴标签
plt.ylabel('GDP')
# 添加标题
plt.title('四个直辖市GDP大比拼', fontproperties=getChineseFont())
# 添加刻度标签
plt.xticks(range(4), ['北京市', '上海市', '天津市', '重庆市'], fontproperties=getChineseFont())
# 设置Y轴的刻度范围
plt.ylim([5000, 15000])

# 为每个条形图添加数值标签
for x, y in enumerate(GDP):
    plt.text(x, y + 100, '%s' % round(y, 1), ha='center')

# 显示图形
plt.show()
