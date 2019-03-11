class D:
    pass


class E:
    pass


class F:
    pass


class B(D, F):
    pass


class C(F, E):
    pass


class A(B, C):
    pass


# c3算法推演过程
# mro(A) = [A] + merge(mro(B), mro(C), [B, C])
# mro(A) = [A] + merge([B] + merge(mro(D), mro(F), [D, F]), mro(C), [B, C])
# mro(A) = [A] + merge([B] + merge(mro(D), mro(F), [D, F]), [C] + merge(mro(F), mro(E), [F, E]), [B, C])
# mro(A) = [A] + merge([B] + merge([D,object], [F,object], [D,F]), [C] + merge([F,object], [E,object], [F,E]), [B,C])
# mro(A) = [A] + merge([B,D,F,object], [C,F,E,object],[B,C])
# mro(A) = [A, B] + merge([D,F,object], [C,F,E,object],[C])
# mro(A) = [A,B,D] + merge([F,object],[C,F,E,object],[C])
# mro(A) = [A,B,D,C] + merge([F,object],[F,E,object])
# mro(A) = [A,B,D,C,F] + merge([object],[E,object])
# mro(A) = [A,B,D,C,F,E] + merge([object],[object])
# mro(A) = [A,B,D,C,F,E,object]
print(A.__mro__)
