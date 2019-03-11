from collections import deque
# deque是线程安全的
# deque是python中的双端队列
# 传入一个可迭代对象
# 操作方法比list多了首端操作 appendleft, extendleft, popleft
# 可以传入maxlen参数限制队列长度(先进先出原则，当队列溢出，从队首pop)
# [5, 6, 7, 8, 9]
a = deque([1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=5)
print(a)
a = deque('abc')
print(a)

