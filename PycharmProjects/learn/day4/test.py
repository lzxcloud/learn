#!/usr/bin/env python
import copy
dic = {'k':'v',"k2":[11,22,33]}
lst =[1,2,3,4,5,6,7,8,9,dic ]
lstc1 = lst
lstc2=copy.copy(lst)
lstc3=copy.deepcopy(lst)
lst.append("test")
print(lstc1)
print(lstc2)
print(lstc3)
a = "cc"
a.isspace()