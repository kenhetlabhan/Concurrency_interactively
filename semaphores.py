import threading
import time
import random

class Producer_Wo_Sema(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_pointer, out_pointer

    items_produced = 0
    counter = 0

    while items_produced < 30:
      counter += 1
      buffer[in_pointer] = counter
      in_pointer = (in_pointer + 1)%CAPACITY #if in_pointer ends up above capacity it will get deducted from capacity
      print("Producer produced : ", counter)
      time.sleep(0.1)

      items_produced += 1

class Consumer_Wo_Sema(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_pointer, out_pointer, counter


    items_consumed = 0

    while items_consumed < 30:



      item = buffer[out_pointer]
      out_pointer = (out_pointer + 1)%CAPACITY
      print("Consumer consumed item : ", item)




      time.sleep(0.25)

      items_consumed += 1


class Producer(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_pointer, out_pointer
    global mutex, empty, full

    items_produced = 0
    counter = 0

    while items_produced < 30:
      empty.acquire()
      mutex.acquire()
      counter += 1
      buffer[in_pointer] = counter
      in_pointer = (in_pointer + 1)%CAPACITY
      print("Producer produced : ", counter)
      mutex.release()
      full.release()
      time.sleep(0.1)

      items_produced += 1


class Consumer(threading.Thread):
  def run(self):

    global CAPACITY, buffer, in_pointer, out_pointer, counter
    global mutex, empty, full

    items_consumed = 0

    while items_consumed < 30:
      full.acquire()
      mutex.acquire()

      item = buffer[out_pointer]
      out_pointer = (out_pointer + 1)%CAPACITY
      print("Consumer consumed item : ", item)

      mutex.release()
      empty.release()

      time.sleep(0.25)

      items_consumed += 1

CAPACITY = 10
buffer = [69 for i in range(CAPACITY)]
in_pointer = 0
out_pointer = 0
print("""This program will show the Producer/Consumer Problem solved with semaphores. 
This program consists of Producers that produces data and consumers that consume data. It goes on until all the pieces of data have been consumed.
Do you want the program to run with semaphores or not?""")
a = input(">>   ").lower()

if 'yes' in a or 'y' in a:
    producer = Producer()
    consumer = Consumer()
else:
    producer = Producer_Wo_Sema()
    consumer = Consumer_Wo_Sema()
print("""   """)
print("What do you want the buffer capacity to be?")
CAPACITY = int(input(">>   "))
buffer = [69 for i in range(CAPACITY)]

mutex = threading.Semaphore() #The Semaphore Semaphore. This makes sure that only one thread can handle the buffer at the same time. When acquiring the semaphore it changes the value to 0 and other threads can't access the buffer until the semaphore gets released again.
empty = threading.Semaphore(CAPACITY) #A Semaphore used to see if the buffer if full. The starting value is the capacity of the buffer. If a producing thread produces data, it tries to acquire the semaphore. It gets blocked if the semaphore is zero --> the buffer if full.
full = threading.Semaphore(0) #A Semaphore to count how much data is left in the buffer to be consumed. It starts to be zero and the producing threads releases this semaphore while consuming threads acquire it.



consumer.start()
producer.start()

