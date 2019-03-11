from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8]
result = reduce(lambda x, y: x + y, a)
print(result)

b = [(1, 2), (2, -1), (3, 4), (-2, 1), (3, 6), (2, 3), (-2, -3)]

# 第三个参数是初始值
result = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), b, (0, 0))
print(result)
