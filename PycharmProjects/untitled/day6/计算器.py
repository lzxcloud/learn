#!/usr/bin/env python
import re
def cal(li):
    r = eval(str(li))
    return r
oringin = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14)) -(-4*3)/ (16-3*2))"
a = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14)) -(-4*3)/ (16-3*2))"
def f2(oringin):
    result = re.split("\(([^()]+)\)", oringin,1)
    if len(result) == 3:
        before = result[0]
        content = result[1]
        after = result[2]
        r = cal(content)
        new_str = before + str(r) + after
        return f2(new_str)
    else:
        final = cal(oringin)
        print(final)
f2(oringin)
