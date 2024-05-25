import time
from threading import Thread, Lock

class CommonResource:
    def __init__(self) -> None:
        self.value = 0
        self.lock = Lock()

    def process(self, th):
        if self.lock.locked():
            print(th, " found process locked")
            return
        self.lock.acquire()
        print(th, " thread starting")
        v = self.value
        v = v + 1
        time.sleep(2)
        self.value = v
        print(th, " thread exiting")
        self.lock.release()


resource = CommonResource()
t1 = Thread(target=resource.process, args=('t1',))
t2 = Thread(target=resource.process, args=('t2',))

t1.start()
t2.start()

t1.join()
t2.join()

print("Value:", resource.value)
print("DONE!")
