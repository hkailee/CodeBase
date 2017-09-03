#!/usr/local/bin/python3

"""
This alternative threading module for threads has no method equivalent to
_thread.exit(), but since all that the latter does is raise a system-exit
exception, doing the same in threading has the same effect - the threads
exits immediately and silently;
Nonetheless, daemon on with this threading allows exit...
"""

import threading, sys, time

def action():
    sys.exit()              # or raise SystemExit()
    print('not reached')

threading.Thread(target=action).start()
time.sleep(2)
print('Main exit')