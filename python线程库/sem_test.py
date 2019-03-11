import threading, time
from threading import Semaphore
from chapter10.custom_sem import CustomSem
import time

class PrintThread(threading.Thread):

    def __init__(self, sem):
        super().__init__()
        self.sem =sem

    def run(self):
        time.sleep(1)
        print("sem_sample")
        self.sem.release()


class SampleThread(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            print_thread = PrintThread(sem)
            print_thread.start()


if __name__ == '__main__':
    sem = CustomSem(3)
    sample_thread = SampleThread(sem)
    sample_thread.start()
    sample_thread.join()


