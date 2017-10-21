#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
*Description: 字符串类型
*
*Created by liuguoquan on 2017/8/4 17:04
*
"""

import operator

# str类型
a = "Hello,"
print(type(a))

# 单引号也可以
a = 'Hello,'
print(a)

a = """Hello"""
print(a)

a = str("Hello,")
print(a)

# 连接字符串
b = "world!"
print(a + b)

c = 1
# print(a + c)  # failed str 不能直接与int拼接，必须是同一类型
print(a + str(1))  # OK
print(a + repr(1))  # Ok repr转化为字符串


# 控制台输入
# age = input("how are you!\n")
# print(age)


"""
基本操作
"""

# +
a = "study "
b = "python"
print(a + b)

# in
s = "study python"
print("study" in s)  # True
print("just" in s)  # False

# max
s = "studypython"
print(max(s))  # y

# min
print(min(s))  # d

# 大小比较
a = "study "
b = "python"
print(operator.lt(a, b))  # a < b
print(operator.le(a, b))  # a <= b
print(operator.eq(a, b))  # a == b
print(operator.ne(a, b))  # a != b
print(operator.gt(a, b))  # a > b
print(operator.ge(a, b))  # a >= b

# len
print(len(s))  # 11

# * 以指定的次数重复打印字符串
print("hello " * 4)  # hello hello hello hello


"""
字符串方法
"""

print("字符串方法\n")

# isalpha 判断字符串是否全是字母

a = "python"
b = "python1"
print(a.isalpha())
print(b.isalpha())
print(b.isdigit()) # 是否全是数字

# split 根据指定的分隔符分割字符串

s = "zhu*yan*yang"
print(s.split("*"))
print(s.partition("yan"))  # 根据指定的分隔符将字符串进行分割

# strip 去掉两头空格

s = " hello "
print(s.strip())  # 去掉两边
print(s.lstrip())  # 去掉右边空格
print(s.rstrip())  # 去掉左边空格

# 大小写转换

s = "hLlo"
print(s.isupper())  # 是否全部是大写
print(s.islower())  # 是否全部是小写
print(s.upper())  # 全部转换为大写
print(s.lower())  # 全部转换为小写
print(s.capitalize())  # capitalize 首字母变大写
print(s.istitle())  # 首字母是否为大写字母
print(s.swapcase())  # 大写变小写 小写变大写

# join连接字符串

s = "www.baidu.com"
ret = s.split(".")
print("**".join(ret))  # 以指定的分隔符连接

# count 统计字符串里某个字符出现的次数,可选参数为在字符串搜索的开始与结束位置。

print(s.count("w"))
print(s.count("w", 3, 5))

# 编码

temp = "中文"
print(temp.encode("utf-8"))
print(temp.encode("gbk"))

# 判断字符串是否以指定字符开始或者结尾

s = "hell,world"
print(s.startswith("he"))
print(s.startswith("he", 0, 4))
print(s.endswith("d"))
print(s.endswith("d", 0, 20))

# 检查子串出现的位置

s = "hello world"
print(s.find("l"))
print(s.find("l", 5, 20))
print(s.rfind("l"))  # 最后出现的位置
print(s.index("l"))
print(s.rindex("l"))

# 字符串替换

print(s.replace("l", "J"))

"""

索引和切片

"""

# 索引
s = "hello, python!"
print(s[0])
print("hello"[0])

# 切片
s = "hello, python!"
print(s[0:2])  # 从0~2位置的字符串
print(s[0:])  # 0 ~ 结尾
print(s[:9])  # 开始~位置9
print(s[:])  # 完整字符串


"""

格式化字符串

- %s 字符串（采用str()的显示）
- %r 字符串（采用repr（）的显示）
- %c 单个字符
- %b 二进制整数
- %d 十进制整数
- %e 指数（底数为e）
- %f 浮点数

"""

# 占位符个格式化

print("I like %s" % "you")
print("I like you, %d years old!" % 20)
print("I like %s, %d years old!" % ("you", 20))

# format格式化

print("I like {}".format("you"))
print("I like {}, {} years old!".format("you", 20))

# 字典格式化

print("I like %(name)s, %(age)d years old!" % {"name": "you", "age": 20})