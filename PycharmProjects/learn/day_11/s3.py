#!/usr/bin/env python3
#我是一关于进程的测试程序
#进程之间数据共享
import threading
from multiprocessing import  Process
import time

li = []

def foo(i):
    li.append(i)
    print('say hi',li)

for i in range(10):
    p = threading.Thread(target=foo, args=(i,))
    p.start()


