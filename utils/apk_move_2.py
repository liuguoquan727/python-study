#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: apk文件改名移动至指定文件夹 Android Studio 3.0
*
* apk_move 应用名称  版本号
*
* Created by liuguoquan on 2017/8/29 17:40
*
"""

import os
import operator

# 获取当前目录下的文件
apk = os.listdir(os.getcwd())
print(os.getcwd())

for dir1 in apk:
    if os.path.isdir(dir1) & operator.eq(dir1, "apk"):
        print(dir1)
        for dir2 in os.listdir(os.getcwd() + "/" + dir1):
            if os.path.isdir(os.getcwd() + "/" + dir1):
                print(dir2)
                for dir3 in os.listdir(os.getcwd() + "/" + dir1 + "/" + dir2):
                    if os.path.isdir(os.getcwd() + "/" + dir1 + "/" + dir2):
                        print(dir3)
                        for dir4 in os.listdir(os.getcwd() + "/" + dir1 + "/" + dir2 + "/" + dir3):
                            file = os.getcwd() + "/" + dir1 + "/" + dir2 + "/" + dir3 + "/" + dir4
                            if file.endswith(".apk"):
                                print("file path:" + file)
                                command = "cp " + file + " /Users/liuguoquan/Desktop/apk/release"
                                print(command)
                                os.system(command)

# # 移动apk文件
# command = "mv " + newname + " /Users/liuguoquan/Desktop/apk"
# print(command)
# # 执行shell命令
# os.system(command)
