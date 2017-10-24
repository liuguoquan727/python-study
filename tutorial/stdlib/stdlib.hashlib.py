#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 用于加密相关的操作 代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
*
* Created by liuguoquan on 2017/10/23 16:52
*
"""

import hashlib

# md5
md5 = hashlib.md5()
md5.update(bytes("liuguoquan", encoding='utf-8'))
print(md5.hexdigest())

# sha1
sha1 = hashlib.sha1()
sha1.update(bytes("liuguoquan", encoding='utf-8'))
print(sha1.hexdigest())

# sha256
sha256 = hashlib.sha256()
sha256.update(bytes("liuguoquan", encoding='utf-8'))
print(sha256.hexdigest())
