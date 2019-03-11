# import os
# #fork只能用于linux/unix中
# pid = os.fork()
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from concurrent.futures import ProcessPoolExecutor
import time


def fib(n):
    if not isinstance(n, int):
        raise ValueError("必须传入 int")
    if n < 0:
        raise ValueError("传入的数必须大于0")

    if n == 0:
        return 0

    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    start = time.time()
    pool = ThreadPoolExecutor(25)
    # pool = ProcessPoolExecutor(25)
    futures = [pool.submit(fib, i) for i in range(15, 40)]

    wait(fs=futures, return_when=ALL_COMPLETED)
    end = time.time()
    print(end - start)
