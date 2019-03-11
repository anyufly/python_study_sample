"""
python中一切都是对象，包括函数和类，属于Python的一等公民
1、赋值给一个变量
2、可以添加到集合对象中
3、可以作为参数传递给函数
4、可以当做函数的返回值
"""


def print_name(name='jeff'):
    """
    这个函数的作用是打印传入的名字
    :param name: 传入的名字
    :return: None
    """
    print(name)


class NamePrinter:
    """
    这个类的作用是打印名字
    """
    def __init__(self, name):
        self.name = name

    def print_name(self):
        """
        打印名字
        :return:
        """
        print(self.name)


# 将方法赋值给一个变量
my_function = print_name
# 将类赋值给一个变量
my_class = NamePrinter
# 调用方法
my_function('Jack')
# 初始化类
printer = my_class('Rose')
printer.print_name()

list_obj = [print_name, NamePrinter]


def print_type(_obj):
    """
    打印传入对象的类型
    :param _obj: 传入的对象
    :return:
    """
    print(type(_obj))


for obj in list_obj:
    print_type(obj)


def decorator_function(func):
    """
    迭代器的实现,将函数作为参数传入
    :param func:
    :return:
    """
    def wrapper(*args, ** kw):
        """

        :param args:
        :param kw:
        :return:
        """
        print("I'm wrapper!")
        func(*args, **kw)

    # 将函数作为返回值
    return wrapper


def function_sample(sample_name):
    """
    function_sample
    :return:
    """
    print("I'm function_sample：" + str(sample_name))


decorator = decorator_function(function_sample)
decorator('decorator')


