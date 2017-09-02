#!/usr/local/bin/python3

"""
uses mutexes to know when threads are done in parent/main thread,
instead of time.sleep; lock stdout to avoid comingled prints;
"""

import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myID, i))
        stdoutmutex.release()
    exitmutexes[myID].acquire()                 # singal main thread

for i in range(10):                              # spawn 10 threads
    thread.start_new_thread(counter, (i, 100))    # each thread loops 100 times.

for mutex in exitmutexes:
    while not mutex.locked():
        pass

print('Main thread exiting.')