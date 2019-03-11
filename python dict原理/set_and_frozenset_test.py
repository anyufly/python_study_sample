# set是python中的可变集合、frozenset是python中的不可变集合
# 无序、可变
set_obj = set(((1, 2), (3, 4)))
set_obj.add(1)
set_obj.add((1, 2))
set_obj.add(4)
print(len(set_obj))
print(set_obj)
# 无序、不可变
a = frozenset((1, 2, 3, 4, 5))
print(a)
# TypeError: 'frozenset' object does not support item assignment
# a[0] = 3
