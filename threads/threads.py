from time import sleep
import random
from threading import Thread

def counter(id):
    for i in range(5):
        print("ID:", id, " value:", i)
        sleep(random.randint(2, 7))


threads = []
for j in range(4):
    th = Thread(target=counter, args=(j,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()
print("DONE!")