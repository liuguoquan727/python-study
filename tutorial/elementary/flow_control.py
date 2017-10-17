#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*
* Description: 流程控制
*
* Created by liuguoquan on 2017/8/6 11:19
*
"""

"""
if
"""

n = 8

if n > 10:

    print("n > 10")

elif n > 5:

    print("n > 5 && n <= 10")

else:

    print(" n <= 5")


"""
三元运算符

如果条件成立，那么就把值1赋值给var，如果条件不成立，就把值2赋值给var

var = 值1 if 条件 else 值2
"""

n = 5

ret = 5 if n == 6 else 6
print(ret)

"""
for
"""

s = "liuguoquan"

for i in s:
    print(i)


for i in range(len(s)):
    print(s[i])


lst = ["Apple", "Google", "FaceBook"]

for i in lst:
    print(i)

for key, value in enumerate(lst):
    print(key, value)

"""
range
"""

for i in range(0, 10):
    print(i, end=",")  # 不换行
print()

"""
while
"""

flag = True

if flag:
    print("I like you!")
else:
    print("I do not like you !")


# break

i = 10

while i:

    if i % 2 == 0:
        break
    else:
        print("%d is odd number!" % i)
        i = 0

print("%d is even number!" % i)


# continue

i = 10

while i:

    if i % 2 == 0:
        print("%d is even number!" % i)
        i -= 1
        continue
    else:
        print("%d is odd number!" % i)
        i -= 1



