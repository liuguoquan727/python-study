#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: time模块 时间
*
* Created by liuguoquan on 2017/10/21 17:24
*
"""

import time

"""
time.sleep(int)	等待时间
time.time()	输出时间戳，从1970年1月1号到现在用了多少秒
time.ctime()	返回当前的系统时间
time.gmtime()	将时间戳转换成struct_time格式
time.localtime()	以struct_time格式返回本地时间
time.mktime(time.localtime())	将struct_time格式转回成时间戳格式
time.strftime(“%Y-%m-%d %H:%M:%S”,time.gmtime())	将struct_time格式转成指定的字符串格式
time.strptime(“2016-01-28”,”%Y-%m-%d”)	将字符串格式转换成struct_time格式
"""

print(time.time())
print(time.ctime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
