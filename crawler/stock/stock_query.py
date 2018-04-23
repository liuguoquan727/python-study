#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 股票查询
*
* Created by liuguoquan on 2018/4/18 10:41
*
"""
# import sys
# sys.path.append("/Users/liuguoquan/workspace/study/python-study/crawler/stock/package_stock")
import requests
import json
import time
# import stock_response
import mysql.connector as connector


# from stock_response import StockResponse, Result, Data


class StockResponse(object):
    def __init__(self):
        self.resultcode = 0
        self.reason = ""
        self.error_code = 0
        self.result = []


class Data(object):
    def __init__(self):
        self.date = ""
        self.time = ""
        self.gid = ""
        self.name = ""
        self.nowPri = ""


class Result(object):
    def __init__(self):
        self.data = None


def totimemills(timestr):
    # 转换成时间数组
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return int(timestamp) * 1000


class Stock(object):
    def __init__(self):
        self.name = ""
        self.chn = ""
        self.gid = ""


db = connector.connect(user='root', password='Lgq0604030123!', database='stock')

cursor = db.cursor()

# 解析json
f = open("/Users/liuguoquan/workspace/study/python-study/crawler/stock/stock.json", encoding="utf-8")
value = f.read()

stocks = []

stocks = json.loads(value)

for item in stocks:
    cursor.execute("select * from stock_name")
    stockNames = cursor.fetchall()
    isInsert = False
    stock = Stock()
    stock.__dict__ = item
    if len(stockNames) == 0:
        isInsert = True
    else:
        isInsert = True
        for stockName in stockNames:
            if stockName[0] == stock.gid:
                isInsert = False
                break
    if isInsert:
        sql = "INSERT INTO stock_name(gid ,name) VALUES ('%s','%s')" % (stock.gid, stock.chn)
        cursor.execute(sql)
        db.commit()

param = {'gid': "", "key": "c1d4b5f28c4c5642aaca35895283452a"}

print("******开始******")

isOpen = True

if isOpen:
    for item in stocks:
        stock = Stock()
        stock.__dict__ = item
        param['gid'] = stock.gid
        response = requests.get("http://web.juhe.cn:8080/finance/stock/hs", params=param)
        stockResponse = StockResponse()
        stockResponse.__dict__ = json.loads(response.text)
        if int(stockResponse.resultcode) == 200:
            for result in stockResponse.result:
                stockResult = Result()
                stockResult.__dict__ = result
                stockData = Data()
                stockData.__dict__ = stockResult.data
                print(stockData.name)
                print(stockData.nowPri)
                print(stockData.gid)
                timeStr = stockData.date + " " + stockData.time
                timstamp = totimemills(timeStr)
                sql = "INSERT INTO STOCK_HISTORY(gid, \
                       name, time_stamp, price,date_time) \
                       VALUES ('%s', '%s', '%d', '%s','%s')" % \
                      (stockData.gid, stockData.name, timstamp, stockData.nowPri, timeStr)
                cursor.execute(sql)
                db.commit()

cursor.close()
db.close()
print("******结束******")
