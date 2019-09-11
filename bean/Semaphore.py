import threading
from queue import Queue

class Mutex_Semaphore():

    def __init__(self): #padrão mutex.
        self.process_queue = Queue()
        self.count = 1

    def wait(self, lock):
        self.count -= 1
        if not(lock.locked()):
            lock.acquire()

        if self.count < 0:
            self.lock(lock)

    def done(self):
        self.count += 1
        if self.count <= 0:
            self.unlock()

    def lock(self, lock):
        self.process_queue.put(lock)
        lock.acquire()

    def unlock(self):
        lock = self.process_queue.get()
        lock.release()




        



