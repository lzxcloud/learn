#!/usr/bin/env python3
l1 = ["alex",22,33,44,55]
l2 = ["is",22,33,44,55]
l3 = ["good",22,33,44,55]
l4 = ["guy",22,33,44,55]

s1 =zip(l1,l2,l3,l4)
s2 = []
for i in list(s1)[0]:
    if i == "guy":
        s2.append(i)
        break
    s2.append(i + '-')
finalstr="".join(s2)
print(finalstr)