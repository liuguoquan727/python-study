#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: mysql数据库操作
*
* Created by liuguoquan on 2017/10/24 09:44
*
"""

import mysql.connector as connector

conn = connector.connect(user='root', password='2436363', database='test')

cursor = conn.cursor()

cursor.execute("select * from student")

values = cursor.fetchall()

print(values)

conn.close()
