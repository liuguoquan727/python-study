#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description:
*
* Created by liuguoquan on 2017/11/22 11:40
*
"""

import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()
print(str(sess.run(hello)))
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
sess.close()
