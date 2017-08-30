########## First scanner ##########
def scanner1 (name, function):
    file = open(name, 'r')              # create a file object
    while True:
        line = file.readline()          # call file method
        if not line: break              # until end-of-file
        function(line)                  # call a function object
    file.close()

########## Second scanner ##########
# Recommended for higher speed using for loop than the above while loop
def scanner2(name, function):
    for line in open(name, 'r'):        # scan line-by-line
        function(line)                  # call a function