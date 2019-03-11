import threading
from queue import Queue

total = 0
q = Queue(maxsize=1000)
# q.put(total)


def add():
    global total
    # total = q.get()
    for i in range(1000000):
        total += 1
    q.put(total)


def sub():
    global total
    total = q.get()
    for i in range(1000000):
        total -= 1
    q.task_done()


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=sub)

thread1.start()
thread2.start()
thread1.join()
q.join()

print("最终结果：" + str(total))