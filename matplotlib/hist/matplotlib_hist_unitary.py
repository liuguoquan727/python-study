#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 一元直方图
*
* Created by liuguoquan on 2018/4/17 10:17
*
"""

"""
plt.hist(x, bins=10, range=None, normed=False, 
        weights=None, cumulative=False, bottom=None, 
        histtype='bar', align='mid', orientation='vertical', 
        rwidth=None, log=False, color=None, 
        label=None, stacked=False)
        
x：指定要绘制直方图的数据；
bins：指定直方图条形的个数；
range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；
normed：是否将直方图的频数转换成频率；
weights：该参数可为每一个数据点设置权重；
cumulative：是否需要计算累计频数或频率；
bottom：可以为直方图的每个条形添加基准线，默认为0；
histtype：指定直方图的类型，默认为bar，除此还有’barstacked’, ‘step’,  ‘stepfilled’；
align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
orientation：设置直方图的摆放方向，默认为垂直方向；
rwidth：设置直方图条形宽度的百分比；
log：是否需要对绘图数据进行log变换；
color：设置直方图的填充色；
label：设置直方图的标签，可通过legend展示其图例；
stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放；
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager, FontProperties


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


age = [10, 10, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 4, 30, 15, 15, 15]

plt.style.use("ggplot")

plt.title("乘客年龄分布直方图", fontproperties=getChineseFont())

plt.hist(age, bins=20, color="green", edgecolor="k", rwidth=0.5, label="hist")

plt.tick_params(top="off", right="off")

plt.ylabel("人数", fontproperties=getChineseFont())

plt.xlabel("年龄", fontproperties=getChineseFont())

plt.legend()

plt.show()
