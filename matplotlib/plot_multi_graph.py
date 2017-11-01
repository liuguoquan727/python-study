#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt

__author__ = 'Michael'

"""
*
* 绘制多个子图
* Created by Michael on 2017/2/28 15:19.
*
"""

"""
222 第一位表示总共绘制n行，第二位表示每行分多少列，第三位表示图在每列的位置
"""

# 第一行左
plt.subplot(321, facecolor='r')

# 第一行右
plt.subplot(322, facecolor='g')

# 第二行
plt.subplot(312, facecolor='b')

# 第三行
plt.subplot(313, facecolor='b')

plt.savefig("绘制多个子图.png")
plt.show()
