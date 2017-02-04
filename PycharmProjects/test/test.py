#!/usr/bin/env python3
# name = "a.text"
# lista = str.split(name,".")
# print(lista)
#
# local=(str.find(name,"."))
#
# namekuoz1=name[int(str.find(name,".")):]
# print(namekuoz1)
import hashlib
hash = hashlib.md5()
# help(hash.update)
print(hash.update(bytes('admin', encoding='utf-8')))
print(hash.hexdigest())
print(hash.digest())