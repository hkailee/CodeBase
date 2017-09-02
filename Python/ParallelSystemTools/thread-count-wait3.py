#!/usr/local/bin/python3

"""
passes in mutex object shared by all threads instead of globals;
use with context manager statement for auto acquire/release;
sleep calls added to aviod busy loops and simulate real work
"""

import _thread as thread, time

stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myID, count, mutex):            # shared object passed in
    for i in range(count):
        time.sleep(1 / (myID+1))            # diff fractions of second
        with mutex:                         # auto acquire/release: with
            print('[%s] => %s' % (myID, i))
    exitmutexes[myID].acquire()              # global: single main thread

for i in range(numthreads):                              # spawn 5 threads
    thread.start_new_thread(counter, (i, 5, stdoutmutex))    # each thread loops 5 times.

while not all(mutex.locked() for mutex in exitmutexes):
    time.sleep(0.25)

print('Main thread exiting.')