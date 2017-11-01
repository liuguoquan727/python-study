#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from pylab import mpl

mpl.rcParams['font.monospace'] = ['cmmi10']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
__author__ = 'Michael'

"""
*
* 坐标注释
* Created by Michael on 2017/2/28 18:08.
*
"""


def func1(x):
    return 0.6 * x + 0.3


def func2(x):
    return 0.4 * x * x + 0.1 * x + 0.2


def find_curve_intersects(x, y1, y2):
    # 寻找曲线的相交点
    d = y1 - y2
    idx = np.where(d[:-1] * d[1:] <= 0)[0]
    x1, x2 = x[idx], x[idx + 1]
    d1, d2 = d[idx], d[idx + 1]
    return -d1 * (x2 - x1) / (d2 - d1) + x1


space = np.linspace(-3, 3, 100)
f1 = func1(space)
f2 = func2(space)
plt.figure(figsize=(8, 5))
plt.plot(space, f1)
plt.plot(space, f2)

point1 = find_curve_intersects(space, f1, f2)
point2 = find_curve_intersects(space, f1, f2)
plt.plot(point1, func1(point1), "o")
plt.plot(point2, func1(point2), "o")

plt.fill_between(space, f1, f2, where=f1 > f2, facecolor="green", alpha=0.5)

ax = plt.gca()
trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
# plt.fill_between(np.array([point1, point2]), 0, 1, transforms=trans, alpha=0.1)

a = plt.text(0.05, 0.95, '直线和二次曲线的交点')

plt.show()
