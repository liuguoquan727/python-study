#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 异常处理
*
* Created by liuguoquan on 2017/10/20 16:54
*
"""

"""
错误异常的基本结构

try:
    # 主代码块
    pass
except KeyError as e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass
    
执行流程：

如果出现错误，那么就执行except代码块，然后在执行finally
如果没有出现错误，那么就执行else代码块，然后再执行finally
不管有没有出现异常都会执行finally
"""

try:
    i = "123a"
    n = int(i)
    print("你输入的数字是：", n)
# e是Exception的对象，Exception是一个类
except ValueError as e:
    print("输入类型错误，你应该输入一个数字。")
else:
    print("OK")
finally:
    print("end")

# 主动抛出异常 raise

try:
    # 抛出一个异常
    raise IndexError("Index Exception")
except (IndexError, ValueError) as e:
    print(e)
    print(type(e))
    #  传递异常 程序会捕获异常并中断
    #  raise

# 断言

assert 1 == 1


# 自定义异常

class MyError(Exception):
    def __str__(self):
        return "出错了"


try:
    raise MyError()
except MyError as e:
    print(e)
