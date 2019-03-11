class D:
    pass


class B(D):
    pass


class C(D):
    pass


class A(B, C):
    pass


# 遍历执行merge操作的序列
# 如果一个序列的第一个元素，是其他序列中的第一个元素，或不在其他序列出现
# 则从所有执行merge操作序列中删除这个元素，合并到当前的mro中
# mro推演过程
# mro(A) = [A] + merge(mro(B), mro(C), [B, C])
# mro(A) = [A] + merge([B, D, object], [C, D, object], [B, C])
# mro(A) = [A, B] + merge([D, object], [C, D, object], [C])
# mro(A) = [A, B, C] + merge([D, object], [D, object])
# mro(A) = [A, B, C, D, object]
print(A.__mro__)
