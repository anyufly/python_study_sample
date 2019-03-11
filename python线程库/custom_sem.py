from threading import Condition


class CustomSem:
    def __init__(self, count=1):
        self.cond = Condition()
        self.count = count

    def acquire(self):
        with self.cond:
            if self.count == 0:
                self.cond.wait()
            self.count -= 1

    def release(self):
        with self.cond:
            self.count += 1
            self.cond.notify()
