########## First scanner ##########
def scanner1 (name, function):
    file = open(name, 'r')              # create a file object
    while True:
        line = file.readline()          # call file method
        if not line: break              # until end-of-file
        function(line)                  # call a function object
    file.close()


# The following are recommended for higher speed using for loop than the above while loop

########## Second scanner ##########
def scanner2(name, function):
    for line in open(name, 'r'):        # scan line-by-line
        function(line)                  # call a function

########## Third scanner ##########
def scanner3(name, function):
    list(map(function, open(name, 'r')))

########## Third scanner ##########
def scanner4(name, function):
    [function(line) for line in open(name, 'r')]

########## Third scanner ##########
def scanner5(name, function):
    list(function(line) for line in open(name,'r'))