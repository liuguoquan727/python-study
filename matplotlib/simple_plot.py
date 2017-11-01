#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'Michael'

"""
*
* matplotlib.pyplot模块第一个绘图
* Created by Michael on 2017/2/28 11:30.
*
"""

# 0~10中插入100个点
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x ** 2)

# 调用figure创建一个绘图对象，并且使它成为当前的绘图对象。
plt.figure(figsize=(8, 5))

"""
前两个参数表示x，y轴数据
label:给曲线指定一个标签名称
color:表示指定曲线的颜色，可以是英文单词，也可以是'#ff0000',还可以使用值在0~1之间的三个元素的元组表示如(1.0,0.0,0.0)也表示红色
linewidth:指定曲线的宽度，可以不是整数

"""
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)

"""
"b---"指定曲线的颜色和线型，'b'表示蓝色，'---'表示为虚线
"""
plt.plot(x, z, "b--", label="$cos(x^2)$")

# 设置x轴的标题文字
plt.xlabel("Time(s)")

# 设置y轴的标题文字
plt.ylabel("Volt")

# 设置子图的标题
plt.title("PyPlot First Example")

# 设置x、y轴的显示范围
plt.ylim(-1.2, 1.2)

# 显示label标签图示
plt.legend()

# 保存图像到本地 需调用在show的前面
plt.savefig("第一个绘图.png")

# 显示出我们创建的所有绘图对象
plt.show()
