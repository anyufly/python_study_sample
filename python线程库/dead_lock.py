import threading, time
from threading import Lock

lock1 = Lock()
lock2 = Lock()


class CustomThreadOne(threading.Thread):
    def run(self):
        lock1.acquire()
        print("获取lock1")
        print("消耗lock1...")
        time.sleep(1)
        lock2.acquire()
        print("获取lock2")
        print("消耗lock2...")
        lock2.release()
        lock1.release()


class CustomThreadTwo(threading.Thread):
    def run(self):
        lock2.acquire()
        print("获取lock2")
        print("消耗lock2...")
        time.sleep(1)
        lock1.acquire()
        print("获取lock1")
        print("消耗lock1...")
        lock1.release()
        lock2.release()


if __name__ == '__main__':
    thread1 = CustomThreadOne()
    thread2 = CustomThreadTwo()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
