#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 对象特殊成员
*
* Created by liuguoquan on 2017/10/21 11:36
*
"""


class Person:
    # 类的构造方法
    def __init__(self):
        print("Just do it!")

        # 对象的构造方法

    def __call__(self, *args, **kwargs):
        print("My name is Michael!")

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


# 创建一个对象，并且执行类的构造方法
person = Person()

# 执行对象的构造方法
person()

# 先执行类的构造方法，然后在执行对象的构造方法
Person()()

# 自动执行__getitem__方法
person["age"]

# 自动执行__setitem__方法
person["age"] = 28

# 自动执行__delitem__方法
del person["age"]
