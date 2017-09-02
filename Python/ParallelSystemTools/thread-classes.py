#!/usr/local/bin/python3

"""
thread class instances with state and run() for thread's action;
uses higher-level Java-like threading module object join method (not
mutexes or shared global vars_ to know when threads are done in main
parent thread; see library manual for more details on threading;
"""

import threading, _thread

class Mythread(threading.Thread):           # subclass Thread object
    def __init__(self, myID, count, mutex):
        self.myID = myID
        self.count = count                  # per-thread state information
        self.mutex = mutex                  # shared objects, not globals
        threading.Thread.__init__(self)

    def run(self):                          # run provide thread logic
        for i in range(self.count):         # still sync stdout access
            with self.mutex:
                print('[%s] => %s' % (self.myID, i))

stdoutmutex = threading.Lock()              # same as thread.allocate.lock()

threads = []

for i in range(5):
    thread = Mythread(i, 10, stdoutmutex)  # make/start 10 threads
    thread.start()                          # starts run method in a thread
    threads.append(thread)

for thread in threads:
    thread.join()                           # wait for thread exits

print('Main thread exiting')