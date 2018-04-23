#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2018/4/23 15:23
*
"""

import mysql.connector as connector

db = connector.connect(user='root', password='Lgq0604030123!', database='stock')

cursor = db.cursor()

cursor.execute("create table ww(gid varchar(255) primary key ,name varchar(255) not null )")

cursor.execute("create table ff(id int auto_increment primary key,\
 gid varchar(255) ,name varchar(255) not null,\
               price varchar (255),\
               time_stamp bigint,\
               date_time varchar (255))")

cursor.close()
db.close()
