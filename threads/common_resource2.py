import time
from threading import Thread, Lock

class CommonResource:
    def __init__(self) -> None:
        self.value = 0
        self.lock = Lock()

    def locked_task(self, th):
        self.lock.acquire()
        print(th, " thread starting")
        time.sleep(2)
        print(th, " thread exiting")
        self.lock.release()

    def process(self, th, sleeptime):
        for i  in range(10):
            if not self.lock.locked():
                self.locked_task(th)
                time.sleep(1)
            else:
                time.sleep(sleeptime)


resource = CommonResource()
t1 = Thread(target=resource.process, args=('t1', 5))
t2 = Thread(target=resource.process, args=('t2', 6))
t3 = Thread(target=resource.process, args=('t3', 3))
t4 = Thread(target=resource.process, args=('t4', 7))
t5 = Thread(target=resource.process, args=('t5', 15))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("DONE!")
