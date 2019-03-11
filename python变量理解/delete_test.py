
# python中垃圾回收的算法是采用引用计数
# cpython 2.0中的垃圾回收机制采用引用计数为主，分代收集为辅
a = object()
b = a
del a
print(a)
print(b)
