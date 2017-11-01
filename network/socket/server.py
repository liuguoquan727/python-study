#!/usr/bin/env python
# coding=utf-8

"""
*
*
* Created by Michael on 2017/3/17 14:29.
*
"""

import socket

__author__ = 'Michael'

sk = socket.socket()

sk.bind(("127.0.0.1", 6053))

sk.listen(5)

while True:

    conn, address = sk.accept()

    conn.sendall(bytes("Hello, World!", encoding='utf-8'))

    while True:

        print("等待Client...")

        receive = conn.recv(1024)

        strs = str(receive, encoding='utf-8')

        print(strs)

        if strs == "q":
            break

        inp = input("已知道...")
        conn.sendall(bytes(inp, encoding='utf-8'))
