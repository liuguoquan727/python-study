#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 列表类型
*
* Created by liuguoquan on 2017/8/5 10:17
*
"""

import operator

a = []
print(type(a))  # <class 'list'>
print(a)


a = [1, 2, 3, "a", "b"]  # 数组里可以有多种数据类型
print(a)


"""
索引
"""

a = [1, 2, True, "hello"]
print(a[0])
print(a[2])
print(a[3])
print(a.index(1))

"""
切片
"""

lst = ["Java", "Python", "Go", "C++"]
print(lst[-1])
print(lst[-3:-1])
print(lst[:])
print(lst[2:])

print(lst[::-1])  # 反转

"""
list操作
"""

lst = ["Java", "Python", "Go", "C++"]

print(len(lst))  # 长度

alst = ["C", "JavaScript"]

print(lst + alst)   # 序列相加

print(lst * 3)  # 重复n次序列

print("C++" in lst)  # 是否存在某元素

print(max(lst))

print(min(lst))

print(operator.eq(lst, alst))  # 比较


"""
list的方法
"""

lst = ["Java", "Python", "Go", "C++"]

lst.append("C#")  # 追加元素

print(lst)

lst = ["Java", "Python", "Go", "C++"]
alst = ["C#", "C"]

lst.extend(alst)  # 将两个列表合并
print(lst)

lst.insert(len(lst), "Java")  # 指定位置插入元素
print(lst)

print(lst.count("Java"))  # 元素出现的次数

print(lst.index("Java"))  # 元素首次出现的位置

lst.remove("Java")  # 删除列表中首次出现的元素
print(lst)

print(lst.pop(0))  # 删除指定位置的元素并返回

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.reverse() # 列表的元素顺序反过来
print(a)

a = [1, 9, 7, 4, 6, 3, 8]
a.sort()  # 默认从小到大的排序
print(a)

a.sort(reverse=True)  # #从大到小的排序
print(a)

lst = ["Java", "Python", "Go", "C++"]
lst.sort(key=len)  # 字符串长度排序
print(lst)

lst.sort(key=str)  # 按字符串大写排序
print(lst)

lst.clear()  # 清空列表
print(lst)

"""
列表和字符串的相互转化
"""

lst = ["Java", "Python", "Go", "C++"]

print("*".join(lst))  # list 转 str

s = "I like you"
lst = s.split(" ")
print(lst)
print(type(lst))
