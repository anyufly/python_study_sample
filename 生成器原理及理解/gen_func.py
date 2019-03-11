from collections.abc import Iterator


def gen():
    yield 1
    yield 2
    yield 3

# gen_obj = gen()
#
# for i in gen_obj:
#     print(i)


def fib_gen(index):
    """
    斐波那契函数
    :param index: 获取多少位的斐波那契函数
    :return:
    """
    if not isinstance(index, int):
        raise ValueError("Value Error：传入的索引必须为正整数")
    if index <= 0:
        raise ValueError("Value Error：传入的索引必须为正整数")

    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1



