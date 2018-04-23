#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 箱线图
*
* Created by liuguoquan on 2018/4/17 10:15
*
"""

"""
 plt.boxplot(x, notch=None, sym=None, vert=None, 
             whis=None, positions=None, widths=None, 
             patch_artist=None, meanline=None, showmeans=None, 
             showcaps=None, showbox=None, showfliers=None, 
             boxprops=None, labels=None, flierprops=None, 
             medianprops=None, meanprops=None, 
             capprops=None, whiskerprops=None)
             
    x：指定要绘制箱线图的数据；
    notch：是否是凹口的形式展现箱线图，默认非凹口；
    sym：指定异常点的形状，默认为+号显示；
    vert：是否需要将箱线图垂直摆放，默认垂直摆放；
    whis：指定上下须与上下四分位的距离，默认为1.5倍的四分位差；
    positions：指定箱线图的位置，默认为[0,1,2…]；
    widths：指定箱线图的宽度，默认为0.5；
    patch_artist：是否填充箱体的颜色；
    meanline：是否用线的形式表示均值，默认用点来表示；
    showmeans：是否显示均值，默认不显示；
    showcaps：是否显示箱线图顶端和末端的两条线，默认显示；
    showbox：是否显示箱线图的箱体，默认显示；
    showfliers：是否显示异常值，默认显示；
    boxprops：设置箱体的属性，如边框色，填充色等；
    labels：为箱线图添加标签，类似于图例的作用；
    filerprops：设置异常值的属性，如异常点的形状、大小、填充色等；
    medianprops：设置中位数的属性，如线的类型、粗细等；
    meanprops：设置均值的属性，如点的大小、颜色等；
    capprops：设置箱线图顶端和末端线条的属性，如颜色、粗细等；
    whiskerprops：设置须的属性，如颜色、粗细、线的类型等；
"""
