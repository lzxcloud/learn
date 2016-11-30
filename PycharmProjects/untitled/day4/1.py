#!/usr/bin/env python
# 数据库中原有
old_dict = {
    "#1":11,
    "#2":22,
    "#3":100
}

new_dict = {
    "#1":33,
    "#4":22,
    "#7":100
}
old_key=old_dict.keys()
new_key=new_dict.keys()
old_set=set(old_key)
new_set=set(new_key)
del_set=old_set.difference(new_set)
add_set=new_set.difference(old_set)
update_set=old_set.intersection(new_set)

update_set_list=list(update_set)
add_set_list=list(add_set)
del_set_list=list(del_set)
old_dict[update_set_list[0]]=new_dict[update_set_list[0]]
for i in add_set_list:
    old_dict[i]=new_dict[i]
for i in del_set_list:
    old_dict.pop(i)
print(old_dict)