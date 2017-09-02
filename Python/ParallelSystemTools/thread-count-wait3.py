#!/usr/local/bin/python3

"""
uses simple shared global data (not mutexes) to know when threads
are done in parent/main thread; threads share list but not its items,
assumes list won't move in memory once it has been created initially
"""

import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10

def counter(myID, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myID, i))
        stdoutmutex.release()
    exitmutexes[myID] = True               # singal main thread

for i in range(10):                              # spawn 10 threads
    thread.start_new_thread(counter, (i, 100))    # each thread loops 100 times.

while False in exitmutexes:
    pass

print('Main thread exiting.')