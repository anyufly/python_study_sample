import multiprocessing


def fib(n):
    if not isinstance(n, int):
        raise ValueError("必须传入int类型")
    if n < 0:
        raise ValueError("必须传入大于0的整数")
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib(n-1) + fib(n-2)


def finish(value):
    print(f"进程运行结束, 结果是{value}")


if __name__ == '__main__':
    import random
    progress = multiprocessing.Process(target=fib, args=(random.randint(0, 10),))
    print(progress.pid)
    progress.start()
    print(progress.pid)
    progress.join()

    import os
    pool = multiprocessing.Pool(os.cpu_count())
    pool.apply_async(fib, args=(random.randint(1, 10),), callback=finish)
    pool.apply_async(fib, args=(random.randint(1, 10),), callback=finish)
    pool.apply_async(fib, args=(random.randint(1, 10),), callback=finish)

    fib_25 = pool.apply_async(fib, args=(25, ))
    # 使用get获取进程结果，该方法会阻塞主线程
    print(fib_25.get())

    for data in pool.imap(fib, [1, 2, 3]):
        print(data)

    for data in pool.imap_unordered(fib, [30, 10, 1]):
        print(data)

    pool.close()
    # 调用join前一定要关闭进程池
    pool.join()
