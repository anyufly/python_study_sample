from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed
# from concurrent.futures._base import wait
# from concurrent.futures import wait
import threading
import time


def print_thread(n):
    time.sleep(n)
    return f"sleep {n} second"


if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)

    futures = [pool.submit(print_thread, i) for i in range(6, 0, -1)]
    # print(futures[5].cancel())

    # 使用as_completed会使主线程阻塞 （输出顺序与线程执行完成顺序有关）
    # 每执行完一个线程打印一次
    for future in as_completed(fs=futures):
        print(future.result())

    # 使用ThreadPoolExecutor.map()会使主线程阻塞 （输出顺序为 第二个参数的顺序）
    # 所有线程执行完才打印
    for result in pool.map(print_thread, range(6, 0, -1)):
        print(result)

    # 使用wait()方法阻塞主线程
    wait(fs=futures, return_when=ALL_COMPLETED)
    print("线程池所有线程执行完成")

