#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2018/4/18 11:19
*
"""

"""
{
    "resultcode": "200",
    "reason": "SUCCESSED!",
    "result": [
        {
            "data": {
                "buyFive": "600",
                "buyFivePri": "69.690",
                "buyFour": "1000",
                "buyFourPri": "69.730",
                "buyOne": "1500",
                "buyOnePri": "70.000",
                "buyThree": "2100",
                "buyThreePri": "69.800",
                "buyTwo": "100",
                "buyTwoPri": "69.810",
                "competitivePri": "70.000",
                "date": "2018-04-18",
                "gid": "sz300672",
                "increPer": "2.33",
                "increase": "1.600",
                "name": "国科微",
                "nowPri": "70.200",
                "reservePri": "70.190",
                "sellFive": "100",
                "sellFivePri": "70.400",
                "sellFour": "3000",
                "sellFourPri": "70.360",
                "sellOne": "800",
                "sellOnePri": "70.190",
                "sellThree": "900",
                "sellThreePri": "70.330",
                "sellTwo": "3300",
                "sellTwoPri": "70.200",
                "time": "10:41:00",
                "todayMax": "72.600",
                "todayMin": "68.090",
                "todayStartPri": "69.990",
                "traAmount": "245895019.720",
                "traNumber": "34666",
                "yestodEndPri": "68.600"
            },
            "dapandata": {
                "dot": "70.20",
                "name": "国科微",
                "nowPic": "1.600",
                "rate": "2.33",
                "traAmount": "24589",
                "traNumber": "34666"
            },
            "gopicture": {
                "minurl": "http://image.sinajs.cn/newchart/min/n/sz300672.gif",
                "dayurl": "http://image.sinajs.cn/newchart/daily/n/sz300672.gif",
                "weekurl": "http://image.sinajs.cn/newchart/weekly/n/sz300672.gif",
                "monthurl": "http://image.sinajs.cn/newchart/monthly/n/sz300672.gif"
            }
        }
    ],
    "error_code": 0
}
"""


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
