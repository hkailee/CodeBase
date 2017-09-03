#!/usr/local/bin/python3

"""
typically used within a forked child process on Unix
"""

def outahere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')

if __name__ == '__main__':
    outahere()

