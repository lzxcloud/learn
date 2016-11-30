#!/usr/bin/env python
def outer(func):
    def inner(*args, **kwargs):
        print("123")
        ret = func(*args, **kwargs)
        print("456")
        return ret
    return inner
@outer
def f1(a1):
    print("fuzai")
    return a1
print(f1(1))