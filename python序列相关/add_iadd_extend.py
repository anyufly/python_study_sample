# 使用 + 号需要用一个新的变量来接收结果
# 对应的魔法函数为 __add__()
# 只能使用 + 操作相同类型的对象 如 不能使用 a = list + tuple
a = [1, 2, 3]
# TypeError: can only concatenate list (not "tuple") to list
# b = a + (4, 5, 6)
b = a + [4, 5, 6]
# [1, 2, 3]
print(a)

# 使用 += 实现的是就地加,不需要使用一个新的变量来接收结果
# 对应的魔法函数为 __iadd__()
# 可以使用 += 来操作一个可迭代对象
# 其内部实现原理为调用extend()函数
a += (4, 5, 6)
print(a)

# 使用extend()函数实现的是就地加，可以传入一个可迭代对象，内部实现原理为
# 迭代传入的可迭代对象，然后调用append()方法
a.extend((4, 5, 6))
print(a)
