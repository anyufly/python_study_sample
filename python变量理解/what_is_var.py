# import sys
# python变量的实质是一个指针
# a 指向1所对应的内存空间
# 先生成对象 1 ，再使a指向 1对应的内存空间
a = 1

a = [1, 2, 3]
b = a
b.append(4)
# print(a)
# True
print(a is b)
print('============================')
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
# False
print(a is b)
print('============================')
# python  inter机制
# 值比较小的int、小段的字符串 python解释器在启动的时候会生成全局唯一的内存空间
a = 1
b = 1
# True
print(a is b)
print('============================')

a = 2
b = 1
# True
print(b + 1 is a)
print('============================')

a = (1, 2, 3)
b = (1, 2, 3)
# True
print(a is b)
print('============================')

a = 1.2
b = 1.2
# True
print(a is b)
print('============================')

a = frozenset([1, 2, 3, 4, 5])
b = frozenset([1, 2, 3, 4, 5])
# False
print(a is b)
print('============================')

# True
# 编译时求值
print('op' + 'q' is 'opq')
print('============================')
c = 'op'
# False
# 运行时求值
print(c + 'q' is 'opq')
print('============================')
