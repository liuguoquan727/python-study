#!/usr/bin/env python
# coding=utf-8

"""
*
* 对数坐标图
* Created by Michael on 2017/3/1 14:41.
*
"""

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'Michael'

plt.figure(figsize=(8, 7))

w = np.linspace(0.1, 1000, 1000)
p = np.abs(1 / (1 + 0.1j * w))  # 计算低通滤波器的频率响应

ax1 = plt.subplot(221)
ax1.set_title("Normal")
plt.plot(w, p, linewidth=2)
plt.ylim(0, 1.5)

# x轴的对数坐标
ax2 = plt.subplot(222)
ax2.set_title("X-log")
plt.semilogx(w, p, linewidth=2)
plt.ylim(0, 1.5)

# y轴为对数坐标
ax3 = plt.subplot(223)
ax3.set_title("Y-log")
plt.semilogy(w, p, linewidth=2)
plt.ylim(0, 1.5)

# x轴 y轴都为对数坐标
ax4 = plt.subplot(224)
ax4.set_title("XY-log")
plt.loglog(w, p, linewidth=2)
plt.ylim(0, 1.5)

plt.savefig("对数坐标图.png")
plt.show()
