#!/usr/local/bin/python3

"""
typically used within a forked child process on Unix;
Unlike sys.exit, os._exit is immune to both try/except and try/finally interception,
i.e. the calliing process will exits immediately instead of raising and exception
that could be trapped and ignored. In fact, the process also exit without flushing
output stream buffers or running cleanup handlers.
"""

def outahere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')

if __name__ == '__main__':
    outahere()
