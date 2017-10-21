#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2017/10/20 17:14
*
"""


class Person:
    # 公有静态字段
    PublicMembers = "公有静态字段"
    # 私有静态字段 两个下划线
    __PrivateMembers = "私有静态字段"

    # 进入类的时候首先执行__init__方法
    # __init__为构造方法
    def __init__(self, name, age):
        # 类中创建成员变量
        # __xx 下划线表示私有成员变量
        self.__Name = name
        self.Age = age

    def get_name(self):
        return self.__Name

    def set_name(self, name):
        self.__Name = name

    def get_age(self):
        return self.Age

    def set_age(self, age):
        self.Age = age

    def info(self):
        print("""My name is: %s \nMy age is: %d""" % (self.__Name, self.Age))

    # 静态方法括号内没有self，切方法前一行要加上@staticmethod
    @staticmethod
    def static():
        print("静态方法")

    # 创建类方法的时候需要在方法前面加上@classmethod
    @classmethod
    def class_method(cls):  # 类方法的参数是当前类的类名
        print("类方法")


person = Person("liu", 28)
print(person.get_name())
print(person.get_age())
person.info()
person.set_name("zhang")
person.set_age(30)
person.info()
print(Person.PublicMembers)

# 通过特殊的方法去访问类中的私有成员
print(person._Person__Name)  # 一个下划线，一个类名，私有的变量名
print(person._Person__PrivateMembers)

person.static()
Person.static()
person.class_method()
Person.class_method()
