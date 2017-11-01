#!/usr/bin/env python
# coding=utf-8

"""
*
*
* Created by Michael on 2017/3/17 14:39.
*
"""

import socket

__author__ = 'Michael'

obj = socket.socket()

obj.connect(("127.0.0.1", 6053))

# 阻塞，等待服务端发送内容，接受服务端发送过来的内容，最大接受1024字节
ret_bytes = obj.recv(1024)
# 因为服务端发送过来的是字节，所以我们需要把字节转换为字符串进行输出
ret_str = str(ret_bytes, encoding="utf-8")
# 输出内容
print(ret_str)
while True:
    # 当进入连接的时候，提示让用户输入内容
    inp = input("Client请输入要发送的内容>>> ")
    # 如果输出q则退出
    if inp == "q":
        # 把q发送给服务端
        obj.sendall(bytes(inp, encoding="utf-8"))
        # 退出当前while
        break
    else:
        # 否则就把用户输入的内容发送给用户
        obj.sendall(bytes(inp, encoding="utf-8"))
        # 等待服务端回答
        print("正在等待Server输入内容......")
        # 获取服务端发送过来的结果
        ret = str(obj.recv(1024), encoding="utf-8")
        # 输出结果
        print(ret)
# 连接完成之后关闭链接
obj.close()
