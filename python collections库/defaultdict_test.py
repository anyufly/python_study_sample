from collections import defaultdict


def gen_order():
    return '0'


# 传入一个callable对象
# 实现原理是在__getitem__()时会调用魔法函数__missing__()
# __missing__()中会调用我们传进去的callable对象
# 设置字典的默认值为callable对象调用的返回值
# default_dict = defaultdict(int)
# default_dict = defaultdict(str)
default_dict = defaultdict(gen_order)


default_dict['a']
default_dict['b']
default_dict['c']
