import threading
import time
import random

# Shared Memory variables
CAPACITY = 0
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0


# Declaring Semaphores
mutex = threading.Semaphore() #The Semaphore Semaphore. This makes sure that only one thread can handle the buffer at the same time. When acquiring the semaphore it changes the value to 0 and other threads can't access the buffer until the semaphore gets released again.
empty = threading.Semaphore(CAPACITY) #A Semaphore used to see if the buffer if full. The starting value is the capacity of the buffer. If a producing thread produces data, it tries to acquire the semaphore. It gets blocked if the semaphore is zero --> the buffer if full.
full = threading.Semaphore(0) #A Semaphore to count how much data is left in the buffer to be consumed. It starts to be zero and the producing threads releases this semaphore while consuming threads acquire it.

# Producer Thread Class
class Producer(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full

    items_produced = 0
    counter = 0

    while items_produced < 20:
      empty.acquire()
      mutex.acquire()

      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)

      mutex.release()
      full.release()

      time.sleep(random.random())

      items_produced += 1

# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full

    items_consumed = 0

    while items_consumed < 20:
      full.acquire()
      mutex.acquire()

      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)

      mutex.release()
      empty.release()
      time.sleep(random.random())

      items_consumed += 1

# Producer Thread Class without Semaphores
class Producer_Wo_Sema(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full

    items_produced = 0
    counter = 0

    while items_produced < 20:


      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)
      time.sleep(random.random())

      items_produced += 1

# Consumer Thread Class without Semaphores
class Consumer_Wo_Sema(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full

    items_consumed = 0

    while items_consumed < 20:

      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)
      time.sleep(random.random())
      items_consumed += 1


print("""This program will show the Producer/Consumer Problem. Do you want the program to run with semaphores or not?""")
a = input(">>   ").lower()
if 'yes' in a or 'i' in a:
    producer = Producer()
    consumer = Consumer()
else:
    producer = Producer_Wo_Sema()
    consumer = Consumer_Wo_Sema()

print("What do you want the buffer capacity to be?")
CAPACITY = int(input())
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
# Starting Threads
consumer.start()
producer.start()

# Waiting for threads to complete
producer.join()

