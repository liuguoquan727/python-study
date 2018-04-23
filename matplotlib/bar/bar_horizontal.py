#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 水平条形图
*
* Created by liuguoquan on 2018/4/3 11:23
*
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager, FontProperties


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


# 构建数据
price = [38, 48, 68, 58]

# 绘图
plt.barh(range(4), price, 0.5, align='center', color='red', alpha=0.8)
# 添加轴标签
plt.xlabel('价格', fontproperties=getChineseFont())
# 添加标题
plt.title('不同平台的书籍价格比较', fontproperties=getChineseFont())
# 添加刻度标签
plt.yticks(range(4), ['天猫', '京东', '当当', '亚马逊'], fontproperties=getChineseFont())
# 设置X轴的刻度范围
plt.xlim([30, 80])

# 为每个条形图添加数值标签
for x, y in enumerate(price):
    plt.text(y + 1, x, '%s' % y, va='center')

# 显示图形
plt.show()
