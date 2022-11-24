import multiprocessing 


def small(condition):
    print('small process starting')
    with condition:           #with this we aquired the condition
        condition.notify()    # notifying the waiting process that the wait is over

condition = multiprocessing.Condition() #formed a condition
print('main process waiting')
with condition:
    startup=multiprocessing.Process(target=small, args=(condition,))
    startup.start()
    condition.wait() # waiting to be notified, forever if not notified by default can be removed by using timeout function
print('all done')
