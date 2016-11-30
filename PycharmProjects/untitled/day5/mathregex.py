#!/usr/bin/env python
import re
#match()无分组的
oringin = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/$*2998 +10 * 568/14)) -(-4*3)/ (16-3*2))"
n = re.split("\( ([^()+])\)",oringin,1)
print(n)