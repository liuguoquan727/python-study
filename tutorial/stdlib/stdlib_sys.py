#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: sys模块 用于提供对解释器相关的操作
*
* Created by liuguoquan on 2017/10/21 16:24
*
"""

import sys

"""
sys.argv	传递到Python脚本的命令行参数列表，第一个元素是程序本身路径
sys.executable	返回Python解释器在当前系统中的绝对路径
sys.exit([arg])	程序中间的退出，arg=0为正常退出
sys.path	返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform	返回操作系统平台名称，Linux是linux2，Windows是win32
sys.stdout.write(str)	输出的时候把换行符\n去掉
val = sys.stdin.readline()[:-1]	拿到的值去掉\n换行符
sys.version	获取Python解释程序的版本信息
"""

print(sys.version)
print(sys.platform)
