#!/usr/bin/env python3
from multiprocessing import Pool
import time

pools = Pool(5)

def f1(a):
    time.sleep(1)
    print(a)
for i in range(40):
    ret = pools.apply_async(func=f1, args=(11,))
    pools.close()
    pools.join()