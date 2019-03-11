import dis
import inspect

foo_frame = None
bar_frame = None


# python.exe会用一个叫做 PyEval_EvalFramEx(c函数)去执行foo函数， 首先会创建一个栈帧(stack frame)(上下文)
def foo():
    """
    在Python中栈帧也是一个对象（字节码也是个对象），从栈帧对象的上下文中运行foo()函数的字节码
    当foo调用子函数 bar， 又会创建一个栈帧，将函数的控制权交给这个栈帧对象，然后运行这个栈帧上下文bar()函数的字节码
    所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在（关键）
    """
    print("~foo~")
    bar()
    global foo_frame
    # 栈帧对象
    foo_frame = inspect.currentframe()

def bar():
    print("~bar~")
    global bar_frame
    # 栈帧对象
    bar_frame = inspect.currentframe()

# 使用dis.dis 查看字节码
dis.dis(foo)
dis.dis(bar)


foo()
print('func_name：{}\tback_func_name：{}'.format(foo_frame.f_code.co_name, foo_frame.f_back.f_code.co_name))
print('func_name：{}\tback_func_name：{}'.format(bar_frame.f_code.co_name, bar_frame.f_back.f_code.co_name))


def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 30
    yield 3
    # 可以返回，但无意义"
    return "123"


gen = gen_func()
dis.dis(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
