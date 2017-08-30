#!/usr/local/bin/python3

from sys import argv
from scanfile import scanner2

class UnknownCommand(Exception):
    pass

######### Method One ########
def processLine1(line):                  # define a function
    if line[0] == '*':                  # applied to each line
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])        # strip first and last char: \n
    else:
        raise UnknownCommand(line)


######## Method Two ########
commands = {'*': 'Ms.', '+': 'Mr.'}     # expanding the definition
def processLine2(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)

if __name__ == '__main__':
    filename = 'data.txt'
    if len(argv) == 2:
        filename = argv[1]                  # allow filename cmd arg
    print("Method One")
    scanner2(filename, processLine1)          # start the scanner with Method One
    print("Method Two")
    scanner2(filename, processLine2)          # start the scanner with Method Two