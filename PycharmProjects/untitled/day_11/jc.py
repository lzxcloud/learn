#!/usr/bin/env python3
import multiprocessing
def f1(a1):
    print(a1)


t = multiprocessing.Process(target=f1, args=(11,))

t.start()
