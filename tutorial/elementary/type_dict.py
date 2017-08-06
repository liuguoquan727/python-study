#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 字典类型-可变数据类型
*
* Created by liuguoquan on 2017/8/6 10:00
*
"""

import copy

"""
字典中的键必须是不可变对象，值可以是任意类的对象。
"""

# 创建字典

person = {"name": "michael", "age": 28, 1: "male"}
print(type(person))
print(person)

person = dict({"name": "michael", "age": 28, "sex": "male"})
print(type(person))
print(person)

seq = ("I", "like", "you")
d = dict.fromkeys(seq, 1)
print(d)


# 添加字典

person["hobby"] = "runing"
print(person)

# 修改字典

person["age"] = 27
print(person)

# 访问字典的值

print(person["age"])

# 字典中键值对的数量

print(len(person))

# 遍历字典

d = {x: x*2 for x in range(0, 10)}
print(d)


"""
字典的方法
"""

person = dict({"name": ["michael", "liu"], "age": 28, "sex": "male"})
print(id(person))

# 浅拷贝
# Python在所执行的复制动作中，如果是基本类型的数据，就在内存中新建一个地址存储，如果不是基本类型，就不会新建一个地址，而是用标签引用原来的对象。

p1 = person.copy()
print(id(p1))
p1["name"].remove("liu")
print(p1)  # name的值也跟着改变了
print(person)

# 深拷贝 无论是基本数据类型还是其他类型都会新建一个地址来存储。
# 修改原对象的值，就不会影响另一个对象的值

p2 = copy.deepcopy(person)
print(id(p2))

# 清空字典

print(p1.clear())


person = dict({"name": "michael", "age": 28, "sex": "male"})

# 返回指定键的值

value = person.get("name")  # 不存在返回None
print(value)

# 添加键值对 不存在则添加，如果存在，则返回已存在的值且不修改

person.setdefault("hobby", "Run")
print(person)

# 更新字典

d = {"age": 27}
person.update(d)
print(person)


# 返回所有的key

print(person.keys())

# 返回所有的值

print(person.values())

# 转换为列表

print(person.items())

# 删除指定给定键所对应的值，返回这个值并从字典中把它移除

ret = person.pop("age")
print(ret)
print(person)

# 随机返回并删除字典中的一对键和值，因为字典是无序的，没有所谓的”最后一项”或是其它顺序。

ret = person.popitem()
print(ret)
print(person)
