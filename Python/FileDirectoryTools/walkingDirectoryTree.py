#!/usr/local/bin/python3

import sys, os

def lister(root):
    for (dirname, subshere, fileshere) in os.walk(root):
        print('[' + dirname + ']')
        for fname in fileshere:
            print(os.path.join(dirname, fname))     # handle one file

if __name__ == '__main__':
    lister(sys.argv[1])