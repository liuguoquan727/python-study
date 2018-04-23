#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 饼状图
*
* Created by liuguoquan on 2018/4/9 16:20
*
"""

"""
https://mp.weixin.qq.com/s?__biz=MzI5NDY1MjQzNA==&mid=2247484843&idx=2&sn=a2f93ecf4a08c16cc6ccc9b38675dc95&chksm=ec5edad6db2953c0d3c478469542677a1588efa6787c4faebde5a82647941ec7d97a0abb873e&scene=21#wechat_redirect
"""

"""
plt.pie(x, explode=None, labels=None, colors=None, 
        autopct=None, pctdistance=0.6, shadow=False, 
        labeldistance=1.1, startangle=None, 
        radius=None, counterclock=True, wedgeprops=None, 
        textprops=None, center=(0, 0), frame=False)

x：指定绘图的数据；
explode：指定饼图某些部分的突出显示，即呈现爆炸式；
labels：为饼图添加标签说明，类似于图例说明；
colors：指定饼图的填充色；
autopct：自动添加百分比显示，可以采用格式化的方法显示；
pctdistance：设置百分比标签与圆心的距离；
shadow：是否添加饼图的阴影效果；
labeldistance：设置各扇形标签（图例）与圆心的距离；
startangle：设置饼图的初始摆放角度；
radius：设置饼图的半径大小；
counterclock：是否让饼图按逆时针顺序呈现；
wedgeprops：设置饼图内外边界的属性，如边界线的粗细、颜色等；
textprops：设置饼图中文本的属性，如字体大小、颜色等；
center：指定饼图的中心点位置，默认为原点
frame：是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置；
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


edu = [0.25, 0.35, 0.3, 0.15, 0.05]
labels = ['High School', 'College', 'Bachelor', 'Master', 'Doctor']

explode = [0, 0.1, 0, 0, 0]  # 用于突出显示大专学历人群
colors = ['#9999ff', '#ff9999', '#7777aa', '#2442aa', '#dd5555']  # 自定义颜色

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0, 4)
plt.ylim(0, 4)

plt.pie(x=edu,  # 数据
        explode=explode,  # 突出的项
        labels=labels,  # 标签
        # colors=colors, # 颜色
        autopct='%.1f%%',  # 设置百分比的格式
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance=1.15,  # 设置项目标签与圆心的距离
        startangle=0,  # 设置饼图的初始角度
        radius=1.5,  # 设置饼图的半径
        counterclock=False,  # 是否逆时针，这里设置为顺时针方向
        center=(2, 2),  # 设置饼图的原点
        frame=1)  # 是否显示饼图的图框，这里设置显示

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())

plt.title("芝麻信用失信用户教育水平分析", fontproperties=getChineseFont())

plt.show()
