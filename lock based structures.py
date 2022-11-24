from random import randint
from threading import Thread
from threading import Lock
 
def function(threadname, lock, data):
    with lock:      # aquiring the lock
        index = randint(0,1)
        data[index] += 1
        print(f'thread {threadname} changed index {index} to {data[index]}')
 
lock = Lock() # creating a lock

data = [0,1]

threads = [Thread(target=function, args=(i, lock, data)) for i in range(20)] #creating threads

for thread in threads:    #starting threads
    thread.start()

print(data)
