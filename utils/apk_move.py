#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: apk文件改名移动至指定文件夹
*
* apk_move 应用名称  版本号
*
* Created by liuguoquan on 2017/8/29 17:40
*
"""

import os
import sys
import time

argv = sys.argv
name = ""
version = ""

date = time.strftime('%m%d-%H%M', time.localtime(time.time()))
print(date)

if len(argv) > 1:
    #应用名称
    name = argv[1]
    print(name)
    # 命令行输入版本号
    version = argv[2]
    print(version)

# 获取当前目录下的文件
apk = os.listdir(os.getcwd())

for name in apk:
    if name.endswith(".apk"):
        print(name)
        names = name.split(".")
        # 拼接新的apk名称
        newname = names[0] + "-" + version + "-" + date + ".apk"
        newname = newname.replace("app", name)
        # 重命名apk文件
        os.rename(name, newname)
        # 移动apk文件
        command = "mv " + newname + " /Users/liuguoquan/Desktop/apk"
        print(command)
        # 执行shell命令
        os.system(command)
