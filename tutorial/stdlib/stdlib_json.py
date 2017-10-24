#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2017/10/23 16:49
*
"""

import json


class B(object):
    def __init__(self):
        self.age = 0
        self.name = ""
        self.sex = ""


class A(object):
    def __init__(self):
        self.code = 2
        self.data = ""
        self.person = []


f = open("/Users/liuguoquan/workspace/study/python-study/tutorial/stdlib/demo.json")
value = f.read()

ret = json.loads(value)
print(type(ret))

a = A()
# 对象转为字典
a.__dict__ = ret
print(a.code)
print(a.data)
print(a.person)
print(type(a.person))

for item in a.person:
    b = B()
    b.__dict__ = item
    print(b.age)
    print(b.name)
    print(b.sex)
