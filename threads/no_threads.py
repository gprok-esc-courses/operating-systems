from time import sleep
import random

def counter(id):
    for i in range(5):
        print("ID:", id, " value:", i)
        sleep(random.randint(2, 7))


for j in range(4):
    counter(j)