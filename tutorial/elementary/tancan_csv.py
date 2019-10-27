#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2018/6/19 11:53
*
"""

import csv

filename = './tancan.csv'

rows = []

with open(filename, 'r', encoding='gbk') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    # for row in reader:
    # test = row[0].decode("gbk").encode("utf-8")
    # print(row)

print(rows)

for row in rows:
    name = str(row[0])
    front = name[0:3]
    if "市" in front:
        row[1] = name[3:7]
    elif "省" in front:
        row[1] = name[3:7]
    elif "县" in front:
        row[1] = name[3:7]
    else:
        row[1] = name[2:6]

print(rows)
print(len(rows))

with open("./tancan_file.csv", "w", encoding="gbk") as f:
    csvwriter = csv.writer(f)
    for row in rows:
        csvwriter.writerow(row)
