#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: Python3内置函数
* https://docs.python.org/3/library/functions.html
* Created by liuguoquan on 2017/10/19 11:39
*
"""

# abs()

"""
返回数字的绝对值，参数可以是整数或浮点数，如果参数是复数，则返回其大小。
"""

print(abs(-1))

# all(iterable)

"""
all()会循环括号内的每一个元素，如果括号内的所有元素都是真的，
或者如果iterable为空，则返回True，如果有一个为假的那么就返回False
"""

print(all([1, 2, 3]))
print(all([0, 1, 2]))
print(all([1, ""]))
print(all([1, "123"]))
print(all([1, None]))

# any(iterable)

"""
循环元素，如果有一个元素为真，那么就返回True，否则就返回False
"""

print(any([1, 2, 3]))
print(any([1, "123"]))
print(any(["", None]))

# bin(x)

"""
将整数x转换为二进制字符串，如果x不为Python中int类型，x必须包含方法__index__()并且返回值为integer
"""

print(bin(11))

# bool(x)

"""
查看一个元素的布尔值，非真即假
"""

print(bool(1))
print(bool(0))

# bytearray([source [, encoding [, errors]]])

"""
返回一个byte数组，Bytearray类型是一个可变的序列，并且序列中的元素的取值范围为 [0 ,255]。

source参数：

如果source为整数，则返回一个长度为source的初始化数组；
如果source为字符串，则按照指定的encoding将字符串转换为字节序列；
如果source为可迭代类型，则元素必须为[0 ,255]中的整数；
如果source为与buffer接口一致的对象，则此对象也可以被用于初始化bytearray.。
"""

b = bytearray(3)
print(b)
c = bytearray("asdasd", encoding="utf-8")
print(c)

# chr(i)

"""
返回一个数字在ASCII编码中对应的字符，取值范围256个
"""

print(chr(65))
print(chr(97))
print(chr(34))

# complex([real[, imag]])

"""
创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数

"""

print(complex(1, 2))  # (1+2j)
print(complex(1))
print(complex("12"))
print(complex("1+2j"))

# dict(**kwarg)

"""
创建一个数据类型为字典
"""

dic = dict({"k1": "123", "k2": "456"})
print(dic)

# dir(object)

"""
返回一个对象中的所有方法
"""

print(dir(str))

# divmod(a, b)

"""
返回的是a/b（除法取整）以及a对b的余数，返回结果类型为tuple

"""

print(divmod(10, 3))

# enumerate(iterable, start=0)

"""
为元素生成下标
"""

li = ["a", "b", "c"]
for n, k in enumerate(li):
    print(n, k)

# eval(expression, globals=None, locals=None)

"""
把一个字符串当作一个表达式去执行
"""

string = "1 + 3"
print(eval(string))

