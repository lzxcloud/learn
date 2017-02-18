#!/usr/bin/env python
import hashlib

# ######## md5 ########
hash = hashlib.md5()
# help(hash.update)
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
print(hash.digest())

# ######## sha1 ########
#
# hash = hashlib.sha1()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())
#
# # ######## sha256 ########
#
# hash = hashlib.sha256()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())
#
# # ######## sha384 ########
#
# hash = hashlib.sha384()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())
#
# # ######## sha512 ########
#
# hash = hashlib.sha512()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())