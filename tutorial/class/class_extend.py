#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 继承
*
* Created by liuguoquan on 2017/10/20 17:54
*
"""


class Person:
    def __init__(self):
        print("通用人")

    def info(self):
        print("人")


class China(Person):
    def info(self):
        print("中国人")


class American(Person):
    def info(self):
        print("美国人")

    def nose(self):
        print("高鼻梁")


class My(American, China):
    def info(self):
        print("我就是我")


china = China()
china.info()

usa = American()
usa.info()

me = My()
me.info()
me.nose()
