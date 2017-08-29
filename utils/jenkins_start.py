#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 启动Jenkins
*
* Created by liuguoquan on 2017/8/17 20:31
*
"""

import os

ret = os.system("java -jar jenkins.war --httpPort=8000")

print(ret)
