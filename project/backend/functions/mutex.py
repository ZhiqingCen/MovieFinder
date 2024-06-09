import threading

class CricticalSection():
    def __init__(self):
        self.sem = threading.Semaphore()
