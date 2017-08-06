#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 集合set类型-不可变数据
*
* Created by liuguoquan on 2017/8/6 10:39
*
"""

"""
集合中不允许有重复的元素
"""

s1 = set("hello")
print(s1)
print(type(s1))

s2 = set(["Hello", "Google", "Google", "Apple"])
print(s2)

# s2[0]  # 不能索引
# s2[0] = "just"  # 不能修改值

"""
集合中的方法
"""

s = set(["a", "b", "c"])

# 添加元素

s.add("d")
# s.add([1, 2])  # 不能添加可变数据类型
print(s)

# 更新集合

s1 = set(["e", "f", "g"])
s.update(s1)
print(s)

# 随机删除一个元素，并返回这个元素

ret = s.pop()
print(ret)

# 删除集合中指定的元素

s.remove("a")
print(s)

# 存在则删除集合中的元素,不存在则不做处理，不抛出异常

s.discard("b")
print(s)

# 清空集合

s.clear()
print(s)


# 不可变的集合，不能修改集合

s = frozenset(["a", "b", "c"])

"""
集合与集合的关系
"""

s1 = set(["a", "b", "c", "d"])
s2 = set(["a", "b", "c", "d", "e"])


print(s1 == s2)  # 是否相等


print(s1.issubset(s2))  # s1是否是s2子集


print(s1.issuperset(s2))  #  s1是否是s2超集


print(s1.union(s2))  # a b 的并集

print(s1.intersection(s2))  # ab的交集

print(s1.difference(s2))  # A相对B的差集 A相对B不同的部分元素集合

print(s1.symmetric_difference(s2))  # ab的差集

