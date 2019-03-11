from time import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name):
    print(func_name)


@decorator
def f2(func_name1, func_name2, **kw):
    print(func_name1, func_name2)
    print(kw)


# f1('12345')
# f2('12345', '54321', a=356, b=123)


def decorator_with_param(*param, **kwparam):
    def decorator(func):
        def wrapper(*args, **kw):
            if 1 in param:
                print('param contains 1')
            else:
                print('param not contains 1')
            flag = False
            for key, value in kwparam.items():
                if key == 'city':
                    flag = True
                    break
                else:
                    continue
            if flag:
                print('kwparam contains city')
            else:
                print('kwparam not contains city')
            func(*args, **kw)
        return wrapper
    return decorator


class ClassDecoratorSample():
    def __init__(self, func):
        self.func = func
        print('ClassDecoratorSample init...')

    def __call__(self, *args, **kw):
        self.func(*args, **kw)
        print('I\'m a Class Decorator!')


@ClassDecoratorSample
@decorator_with_param(2, 4, x=7, province='chengdu')
@decorator
def f3():
    print('f3')

f3()
