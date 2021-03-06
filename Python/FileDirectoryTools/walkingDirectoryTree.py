#!/usr/local/bin/python3

import sys, os

def lister(root):
    for (dirname, subshere, fileshere) in os.walk(root):
        print('[' + dirname + ']')
        for fname in fileshere:
            print(os.path.join(dirname, fname))     # handle one file


# To list file with filtered string
def listerFilter(root):
    matches = []
    for (dirname, subshere, fileshere) in os.walk(root):
        for fname in fileshere:
            if fname.endswith('.py'):
                pathname = os.path.join(dirname, fname)
                if 'import' in open(pathname).read():
                    matches.append(pathname)
    for name in matches:
        print(name)

# list files in dir tree by recursion
def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):
        path = os.path.join(currdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)

if __name__ == '__main__':
    lister(sys.argv[1])
    listerFilter(sys.argv[1])
    mylister(sys.argv[1])