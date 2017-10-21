#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: configparser用于处理特定格式的文件，其本质上是利用open来操作文件。
*
* Created by liuguoquan on 2017/10/21 17:57
*
"""

import configparser

open("file.conf", "w", encoding="utf-8")
config = configparser.ConfigParser()
config.read("file.conf", encoding="utf-8")

# 添加节点

config.add_section("node1")
config.add_section("node2")
config.add_section("node3")

# 检查节点是否存在

print(config.has_section("node1"))

# 删除节点

config.remove_section("node2")

# 设置节点内的键值对

config.set("node1", "name", "liu")
config.set("node1", "age", "28")
config.set("node1", "sex", "male")
config.set("node1", "fav", "play")

# 检查节点内的key是否存在

print(config.has_option("node1", "name"))

# 删除节点内的key

config.remove_option("node1", "fav")

# 将节点写入文件

config.write(open("file.conf", "w"))

# 获取指定节点下指定key的值

print(config.get("node1", "name"))
print(config.get("node1", "age"))
print(config.get("node1", "sex"))

# 获取指定节点下所有的key

print(config.options("node1"))

# 获取指定节点下所有的键值对
print(config.items("node1"))

# 获取所有节点
print(config.sections())
