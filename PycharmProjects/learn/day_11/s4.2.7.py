#!/usr/bin/env python
#-*- coding: utf-8 -*
from multiprocessing import  Process,Array


def Foo(i,temp):
    print id(temp)
    temp[i] = 100+i
    for item in temp:
            print (i,'------->',item)
for i in range(2):
    temp = Array('i', [11, 22, 33, 44])
    p = Process(target=Foo,args=(i,temp))
    p.start()