def add(x, y):
    result = x + y
    return result

a = add(1, 2)
print(a)


def demo(param, *param1, param2=2):
    print(param)
    print(param1)
    print(param2)


def demo1(param, param2=2, *param1):
    print(param)
    print(param1)
    print(param2)

demo(1, 1, 2, 3, 4, 5, param2=5)
