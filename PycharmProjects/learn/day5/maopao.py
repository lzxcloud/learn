#!/usr/bin/env python
li = [13,22,6,99,11]
for j in range(1,len(li)):
    for i in range(len(li) - j ):
        if li[i] > li[i + 1]:
            temp = li[i]
            li[i] = li[i + 1]
            li[i+1] = temp
print(li)
