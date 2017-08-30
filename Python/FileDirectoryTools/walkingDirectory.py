#!/usr/local/bin/python3

import os, glob

# os.open
print(os.popen('ls .').readlines())

for line in os.popen('ls .'):
    print(line[:-1])

print(list(os.popen('ls .')))

print([fname for fname in os.popen('ls .')])

# glob
print(glob.glob('*'))

# os.listdir
print(os.listdir('.'))
print(os.listdir(os.curdir))

# spliting and joining listing results
dirname = os.getcwd()

for file in glob.glob(dirname + '/*'):
    head, tail = os.path.split(file)
    print(head, tail, '=>', ('/dir1/dir2/' + tail))

for file in os.listdir(dirname):
    print(dirname, file, '=>', os.path.join(dirname, file))