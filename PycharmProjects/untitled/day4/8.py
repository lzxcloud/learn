#!/usr/bin/env python
#写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。
fibs = [0, 1]
for i in range(10-2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)