#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 函数
*
* Created by liuguoquan on 2017/10/19 10:14
*
"""

"""
创建函数的语法：

def 函数名(参数):
    ...
    函数体
    ...
    返回值
"""


# 函数

def num(x):
    print(x)


num(4)

# 带返回值的函数

"""
函数return后面是什么值，re就返回什么值，如果没有指定return返回值，
那么会返回一个默认的参数None
"""


def re():
    if 1 == 1:
        return True
    else:
        return False


print(re())


#  函数参数

def add(x, y):
    print(x + y)


add(2, 3)

# 指定参数

"""
默认情况在再函数ret括号内如果要输入函数参数的值，是要按照顺序来的，
但是如果在ret括号内制定的参数的值，那么就不需要按照顺序来了。
"""


def ret(a, b, c):
    print("a", a)
    print("b", b)
    print("c", c)


ret(a="aaa", c="ccc", b="bbb")

# 默认参数

"""
如果给函数创建了默认值，那么有默认值的这个参数必须在最后面定义，
不能够在没有默认参数的值的前面。
"""


def ret(x, y="Hell, world!"):
    print(x, y)


ret(1)  # 调用默认参数
ret(1, "Just do it!")  # 调用传入的参数

# 动态参数

"""
第一种动态参数

定义第一种动态参数需要在参数前面加上一个*号
"""


def ret(*args):
    print(args[0])
    print(args, type(args))


ret(1, 2, 3)

"""
第二种动态参数

定义第二种动态参数需要在参数前面加上两个*号，给参数传参的时候是一个key对应一个value的，
相当于一个字典的键值对，而且返回的类型就是字典类型。

使用两个星号可以将参数收集到一个字典中，参数的名字是字典的键，对应参数的值是字典的值。
"""


def ret(**kwargs):
    print(kwargs, type(kwargs))


ret(k1="123", k2="234")

dic = {"k1": 123, "k2": 456}
ret(**dic)

"""
第三种动态参数

第三种又称为万能的动态参数
"""


def ret(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


ret("11", "22", k1="11", k2="22")

# 参数书写位置

"""
 一般参数–》默认参数–》元组形式–》字典形式
"""


def func(name, age=None, *args, **kwargs):
    print(name, age, args, kwargs)


# 全局变量和局部变量

"""
全局变量可以理解为在当前这个文件内定义的变量，
局部变量则是在函数内定义的变量
"""

n1 = 1


def num():
    n2 = 2
    print(n1)
    print(n2)


num()

"""
定义的全局变量都可以在函数内调用，但是不能再函数内修改，
局部变量在也不能够直接调用，如果要在函数内修改全局变量，那么就需要用到关键字
"""

n1 = 1


def num():
    n2 = 2
    global n1  # 关键字global修饰全局变量后才能在函数中修改全局变量的值
    n1 = 3
    print(n1)
    print(n2)


num()

# nonlocal语句

"""
nonlocal是用来修改嵌套作用域中的变量，类似于global一样，
只需要在嵌套函数中声明变量名即可，
但是这个变量名是必须已经存在的否则就会报错，
如果要修改的变量在作用域中查找不到，
那么不会继续到全局或内置作用域中查找。
"""


def func1(arg1):
    n = arg1
    print(n)

    def func2():
        nonlocal n
        n += 1

    func2()
    print(n)


func1(10)

# Lambda表达式

"""
Lambda（Lambda expressions）表达式是用lambda关键字创建的匿名函数，
Lambda函数可以用于任何需要函数对象的地方，
在语法上，它们被局限于只能有一个单独的表达式。
"""

f = lambda x, y: x + y
print(f(1, 2))


def action(x):
    return lambda y: x + y


result = action(99)
print(result(2))
