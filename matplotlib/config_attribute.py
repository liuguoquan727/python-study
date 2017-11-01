#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'Michael'

"""
*
* 配置图形属性
* Created by Michael on 2017/2/28 14:49.
*
"""

x = np.arange(0, 5, 0.1)
line = plt.plot(x, x * x)[0]
line.set_antialiased(False)
print(line.get_linewidth())  # 返回linewidth属性

lines = plt.plot(x, np.sin(x), x, np.cos(x))
plt.setp(lines, color="red", linewidth=2.0)
print(plt.getp(lines[0], "color"))  # 返回color属性 getp只能对一个对象进行操作
print(plt.getp(lines[0], "linewidth"))
# print(plt.getp(lines[1]))  # 输出全部属性

f = plt.gcf()  # 查看Figure对象的属性
# print(plt.getp(f))

# axes属性是一个列表，它保存图表中的所有子图对象
print(plt.getp(f, "axes"))
print(plt.gca())
print(f.axes)

# 获取字图中的Line2D对象列表
alllines = plt.getp(plt.gca(), "lines")
print(alllines)
print(f.axes[0].lines)
print(alllines[0] == line)  # 第一条曲线为最开始绘制的曲线
print(alllines[1] == lines[0])
print(alllines[2] == lines[1])
print(alllines[0] == lines[1])

# plt.show()
