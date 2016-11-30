#!/usr/bin/env python
def f(due,a1,a2):
    if due == 11:
        return a1
    a3 = a1 + a2
    print(a3)
    r = f(due+1,a2,a3)
    return r
a22=f(0,0,1)
