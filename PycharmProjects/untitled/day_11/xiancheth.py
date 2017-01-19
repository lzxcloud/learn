#!/usr/bin/env python3
import time
import threading


def f0():
    pass

def f1(a1, a2):
    time.sleep(10)
    f0()

t = threading.Thread(target=f1, args=(123, 111,))
t.setDaemon(False)
t.start()

t = threading.Thread(target=f1, args=(123, 111,))
#主线程是否等子线程
t.setDaemon(False)
t.start()

t = threading.Thread(target=f1, args=(123, 111,))
t.setDaemon(False)
t.start()


#改成True 一下就执行了