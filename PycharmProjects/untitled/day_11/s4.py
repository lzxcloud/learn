#!/usr/bin/env python3
from multiprocessing import  Process
import array
temp = array.array('i',[11,22,33,44])

def Foo(i):
    print (id(temp))
    temp[i] = 100+i
    for item in temp:
            print (i,'------->',item)
for i in range(2):
    p = Process(target=Foo,args=(i,))
    p.start()