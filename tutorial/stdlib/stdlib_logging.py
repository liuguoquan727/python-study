#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:便捷记录日志且线程安全
* https://blog.ansheng.me/article/python-standard-library-logging
* Created by liuguoquan on 2017/10/24 09:19
*
"""

import logging

"""
Level	Numeric value
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0

只有大于当前日志等级的操作才会被记录。
"""

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.critical("critical")
logger.error("error")
logger.warning("warning")
logger.info("info")
logger.debug("debug")
