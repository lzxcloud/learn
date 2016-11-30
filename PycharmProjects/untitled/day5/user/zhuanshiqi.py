#!/usr/bin/env python
def outer(func):
    def inner():
        print("hellow")
        print("hellow")
        print("hellow")
        r = func
        print("hellow")
        print("hellow")
        return r
    return inner()
@outer
def f1():
    print("f1")
f1()