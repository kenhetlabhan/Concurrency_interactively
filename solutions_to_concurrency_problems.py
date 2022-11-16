from threading import current_thread
from threading import Thread

#Some useful links: Threading library documentation: https://docs.python.org/3/library/threading.html, Some nice explanation of deadlocks and where I got the idea for this deadlock situation: https://superfastpython.com/thread-deadlock-in-python/#Deadlock_2_Threads_Waiting_on_Each_Other  

#Here you can create functions which will be a solution to the deadlock
#Call them from the main, and likely use the pass the threads as parameters into the solution to solve the deadlock issue

#--------------------------------------------------------
# task to be executed in a new thread
def task(thread):
    print(f'[{current_thread().name}] waiting on [{thread.name}]')
    thread.join()
    with new_thread:
        print("This will not be printed due the deadlock, so if you are seeing the message the deadlock has been solved")

if __name__ == "__main__":
    # get the current thread
    main_thread = current_thread()
    # create the new threads
    new_thread = Thread(target=task, args=(main_thread, ))
    new_thread2 = Thread(target=task, args=(new_thread, ))
    new_thread3 = Thread(target=task, args=(new_thread2, ))
    new_thread4 = Thread(target=task, args=(new_thread3, ))
    # start the new threads
    new_thread.start()
    new_thread2.start()
    new_thread3.start()
    new_thread4.start()
    # run the last thread
    task(new_thread4)
    # Here there is a deadlock, one thread is waiting for the other, the other thread for another thread and so on