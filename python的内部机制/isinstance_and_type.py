# 使用isinstance()做类型判断可以判定该对象继承链上的所有类型
# 使用type()做类型判断只能判定对象当前的类型，不能判定继承链上的其他类型


class A:
    pass


class B(A):
    pass


b = B()
# True
print(isinstance(b, B))
# True
print(isinstance(b, A))
# True
print(type(b) is B)
# False
print(type(b) is A)

