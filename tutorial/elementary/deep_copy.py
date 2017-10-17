#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 深拷贝和浅拷贝
*
* 深浅拷贝分为两部分，一部分是数字和字符串另一部分是列表、元组、字典等其他数据类型。
*
* Created by liuguoquan on 2017/10/17 21:44
*
"""

import copy

"""
数字和字符串

对于数字和字符串而言，赋值、浅拷贝和深拷贝无意义，因为他们的值永远都会指向同一个内存地址。
"""

var1 = 123
print(id(var1))

var2 = var1  # 赋值
print(id(var2))

print(id(var1) == id(var2))  # True

var3 = copy.copy(var2)  # 浅拷贝
print(id(var3))
print(id(var3) == id(var2))  # True

var4 = copy.deepcopy(var2)  # 深拷贝
print(id(var4))
print(id(var4) == id(var2))  # True

"""
其他数据类型

对于字典、元祖、列表 而言，进行赋值、浅拷贝和深拷贝时，其内存地址的变化是不同的。
"""

# 赋值

"""
赋值，只是创建一个变量，该变量指向原来内存地址
"""

var1 = {"a": "1", "b": "2", "c": ["123", "456"]}
var2 = var1  # 赋值后的var2指向var1的内存地址
print(id(var1))
print(id(var2))
print(id(var1) == id(var2))  # True

# 浅拷贝

"""
浅拷贝，内存中只额外创建第一层数据
"""

var1 = {"a": "1", "b": "2", "c": ["123", "456"]}
var2 = copy.copy(var1)  # 浅拷贝

# False 两个变量的内存地址是不一样的
print(id(var1) == id(var2))

# True 两个变量中的元素的内存地址是一样的
print(id(var1["a"]) == id(var2["a"]))

# 深拷贝

"""
深拷贝，在内存中将所有的数据重新创建一份（排除最后一层，即：python内部对字符串和数字的优化）
"""

var1 = {"a": "1", "b": "2", "c": ["123", "456"]}
var2 = copy.deepcopy(var1)  # 深拷贝

# False 两个变量的内存地址是不一样的
print(id(var1) == id(var2))

# False 两个变量中的元素的内存地址也是不一样的
print(id(var1["c"]) == id(var2["c"]))

# True 两个变量中的元素的内存地址是一样的，字符串做了优化，字符串常量只保存一份
print(id(var1["a"]) == id(var2["a"]))
