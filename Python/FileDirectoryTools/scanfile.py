def scanner (name, function):
    file = open(name, 'r')              # create a file object
    while True:
        line = file.readline()          # call file method
        if not line: break              # until end-of-file
        function(line)                  # call a function object
    file.close()