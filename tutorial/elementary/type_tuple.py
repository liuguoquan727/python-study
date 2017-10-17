#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 元组类型
*
* Created by liuguoquan on 2017/8/5 10:57
*
"""

"""
* 元组其中的元素不能更改
* 元组中的元素可以是任何类型的数据
"""

t = (123, "abc", ["Java", "Python"])
print(t)
print(type(t))

t = 3  # int类型
print(type(3))
t = (3, )  # 加逗号表示元组类型
print(type(t))



"""
索引和切片
"""
t = (123, "abc", ["Java", "Python"])
print(t[0])
print(t[:])
print(t[0:])
print(t[2][0])

# t[0] = 24 元组的元素不能修改


"""
列表和元组转换
"""

t = (123, "abc", ["Java", "Python"])
tlst = list(t)  # tuple -> list
print(tlst)
print(type(tlst))

lst = ["Java", "Python", "Go", "C++"]
t = tuple(lst)  # list -> tuple
print(t)
print(type(t))
