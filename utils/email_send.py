#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 发送邮件
*
* Created by liuguoquan on 2017/10/19 10:24
*
"""


def email(mail):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["测试", '465536351@qq.com'])
    msg['To'] = formataddr(["走人", '465536351@qq.com'])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.exmail.qq.com", 465)
    server.login("465536351@qq.com", "lgq2436687471")
    server.sendmail('465536351@qq.com', [mail, ], msg.as_string())
    server.quit()


email("6087414@qq.com")
