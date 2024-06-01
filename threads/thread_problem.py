from threading import Thread, Lock
import time

class Counter:
    def __init__(self) -> None:
        self.value = 0;
        # self.lock = False
        self.lock = Lock()

    def increase(self, thread_id):
        print(i, "starting increase")
        # while(self.lock):
        #     pass
        # self.lock = True
        if self.lock.locked():
            print(i, "found locked")

        self.lock.acquire()
        x = self.value
        x += 1
        time.sleep(5)
        self.value = x
        # self.lock = False
        self.lock.release()
        print(i, "increase completed")



counter = Counter()

threads = []
for i in range(5):
    th = Thread(target=counter.increase, args=(i,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()

print(counter.value)

