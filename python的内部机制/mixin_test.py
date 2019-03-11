

class AMixin:
    """
    mixin模式特点
    1.Mixin类的功能单一
    2 .不和基类关联，可以和任意基类组合，基类可以不和mixin关联就能初始化成功
    3.在mixin中不要使用super的方法
    """
    def func(self):
        pass


class BClass:
    def __init__(self, name):
        self.name = name


class CClass(AMixin, BClass):
    pass
