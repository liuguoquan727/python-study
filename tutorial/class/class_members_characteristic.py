#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 类成员特性
*
* Created by liuguoquan on 2017/10/21 11:46
*
"""

"""
property

把类方法当做普通字段去调用，即用对象调用的时候后面不用加括号

setter

设置类方法的值

deleter

删除类方法的值


"""


class Foo:
    @property
    def characteristic(self):
        print("类的成员特性")

    @characteristic.setter
    def characteristic(self, value):
        print("设置Characteristic的值", value)

    @characteristic.deleter
    def delete(self):
        print("deleter")


foo = Foo()
# 调用类方法的时候方法后面不用加括号
foo.characteristic

# 自动调用 @characteristic.setter 函数
foo.characteristic = 123

# 自动执行 @characteristic.deleter
del foo.delete


# 另一种调用特殊属性的方法

class Person:
    def f1(self):
        print("f1")

    def f2(self, value):
        print("f2")

    def f3(self):
        print("f3")

    SpecialFields = property(fget=f1, fset=f2, fdel=f3, doc="我是注释")


person = Person()

# 调用类的f1方法
person.SpecialFields

# 调用类的f2方法
person.SpecialFields = 3

# 调用类的f3方法
del person.SpecialFields

# 调用类的doc，这里只能通过类去访问，对象无法访问
print(Person.SpecialFields.__doc__)
