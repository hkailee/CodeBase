#!/usr/local/bin/python3

import sys

def filter_files1(name, function):           # filter file through function
    input = open(name, 'r')                 # create file objects
    output = open(name + '.out', 'w')       # explicit output file too
    for line in input:
        output.write(function(line))        # write the modified line
    input.close()
    output.close()                          # output has a '.out' suffix

def filter_stream1(function):                # no explicit files
    while True:                             # use standard streams
        line = sys.stdin.readline()         # or: input()
        if not line: break
        print(function(line), end='')       # or: sys.stdout.write()

# The following are recommended for higher speed using for loop than the above while loop
def filter_files2(name, function):
    with open(name, 'r') as input, open(name, 'r') as output:
        for line in input:
            output.write(function(line))

def filter_stream2(function):
    for line in sys.stdin:
        print(function(line), end='')


if __name__ == '__main__':
    filter_stream1(lambda line: line)        # copy stdin to stdout if run