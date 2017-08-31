#!/usr/local/bin/python3

"""
start programs until you type "1"
"""

import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:                                                # copy process
        os.execlp('python3', 'python3', 'child.py', str(parm))  # overlay program
        assert False, 'error starting program'                  # should not return
    else:
        print('Child is', pid)
        if input() == 'q':
            break