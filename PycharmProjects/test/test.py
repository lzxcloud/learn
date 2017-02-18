#!/usr/bin/env python3
# name = "a.text"
# lista = str.split(name,".")
# print(lista)
#
# local=(str.find(name,"."))
#
# namekuoz1=name[int(str.find(name,".")):]
# print(namekuoz1)
# import hashlib
# hash = hashlib.md5()
# # help(hash.update)
# print(hash.update(bytes('admin', encoding='utf-8')))
# print(hash.hexdigest())
# print(hash.digest())
#
# t1 = 1
# t2 = "a"
#
# print(locals())
#
# num = iter([11,2,23,4])
# for i in num:
#     print(i)


# def f1(x):
# 	if x > 22:
# 		return True
# 	else:
# 		return False
#
# ret = filter(f1,[11,22,33,44])
#
#
# for i in ret:
# 	print(i)
#
# li = [11, 221, 123, 1]
# r = max(li)
# r1 = min(li)
# print(r)
# print(r1)

# v = memoryview(b'abcefg')
# print(v)
# #
#
#
# print(sum([11,33,22]))
# def f1(x):
# 	return x+100
# ret = map(f1,[1,2,3,4,5])
# # for i in ret:
# # 	print(i)
#
# r = reversed([1,2,3,4,5])
# for i in r:
#     print(i)


#没有参数
# print(vars())
#
# class foo:
#     a = 1
# print(vars(foo))
#
# f = foo()
# print(vars(f))


# #对于数字的排序
# li = [1,22,22,3,4]
# #li.sort 会修改原来的list
# li.sort()
# print(li)
# li2 = [1,22,22,3,4]
# #sorted()会再生成一个list
# new_li = sorted(li2)
# print(li2)
# print(new_li)


# li3 = [1,2,4,"6",5]
# li3.sort()
# print(li3)





li4 =["1","5","3","223","1223","A","d","B","_","a","b","abc","张","赵","郭","谢"]
li4.sort()
for i in li4:
    print(bytes(i,encoding="utf-8"))
print(li4)
#
# a = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
# print(a)
# print(sorted("This is a test string from Andrew".split(), key=str.lower))
