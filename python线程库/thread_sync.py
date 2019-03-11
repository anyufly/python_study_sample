import threading
from threading import Lock
total = 0
lock = Lock()

def add():
    global total
    global lock
    with lock:
        for i in range(1000000):
            total += 1


def sub():
    global total
    global lock
    with lock:
        for i in range(1000000):
            total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=sub)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("最终结果：" + str(total))

# 用锁会影响性能
# 锁会引起死锁
# 死锁的情况：A （a, b） B (b, a)