#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2017/10/23 16:46
*
"""

import xml.etree.ElementTree as ET

fd = open("demo.xml")

data = fd.read()

tree = ET.ElementTree(file="/Users/liuguoquan/workspace/study/python-study/tutorial/stdlib/demo.xml")
print
tree

# 获得根元素
root = tree.getroot()
print(root.tag)
print(root.attrib)

# 获得根元素下面的元素
for child in root:
    print(child.tag, child.attrib)
    for gen in child:
        print(gen.tag, gen.text)
