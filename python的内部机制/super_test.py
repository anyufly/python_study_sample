class D:
    def __init__(self):
        # super(D, self).__init__() python2这样写
        print("D")
        super().__init__()


class B(D):
    def __init__(self):
        # super(B, self).__init__() python2这样写
        print("B")
        super().__init__()


class C(D):
    def __init__(self):
        # super(C, self).__init__() python2这样写
        print("C")
        super().__init__()


class A(B, C):
    def __init__(self):
        # super(A, self).__init__() python2这样写
        print("A")
        super().__init__()


# 打印结果为 A B C D ,super()调用的是mro路径的下一个基类的实例
a = A()
