#!/usr/bin/env python
import re
def outer_0(func):
    def inner(*arg, **kwargs):
        print('3.5')
        r = func(*arg, **kwargs)
        print('end')
        return r
    return inner()
def outer(func):
    def inner(*arg, **kwargs):
        print('123')
        r = func(*arg, **kwargs)
        print('456')
        return r
    return inner()

@outer
def index(a1, a2):
    print('fuzi')
    return a1 + a2

# r2 = index('1', '2')
# print(r2)
# re.findall()



