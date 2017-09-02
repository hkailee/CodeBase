#!/usr/local/bin/python3

"""
print 200 each time, because shared resource access synchronized
"""

import threading, time

count = 0

def adder(addlock):             # shared lock object passed in
    global count
    with addlock:               # auto acquire/release around stmt
        count = count + 1       # update a shared name in global scope
    time.sleep(0.5)
    with addlock:               # auto acquire/release around stmt
        count = count + 1           # only 1 thread updating each time

addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)
