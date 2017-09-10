#!/usr/local/bin/python3

"""
pickle to/from flat file utilities
"""

import pickle, io

def saveDbase(filename, object):
    'save object to file'
    file = open(filename, 'wb')
    pickle.dump(object, file)           # pickle to binary file
    file.close()                        # any file-like object will do

def loadDbase(filename):
    'load object from file'
    file = open(filename, 'rb')
    object = pickle.load(file)          # unpickle from binary file
    file.close()                        # re-creates object in memory
    return object

# Create myfile database
L = [0]
D = {'x':0, 'y':L}
table = {'A': L, 'B': D}                # L appears twice
saveDbase('myfile', table)              # serialize to file

# Loading existing myfile database created
table = loadDbase('myfile')
print(table)

# The above are just lists, tuples, and dictionaries. How about class instances?
class Rec:
    def __init__(self, hours):
        self.hours = hours
    def pay(self, rate=50):
        return self.hours * rate

bob = Rec(40)
pickle.dump(bob, open('bobrec', 'wb'))

# Load the bobrec database created above
rec = pickle.load(open('bobrec', 'rb'))
print(rec.hours)
print(rec.pay())


# Pickled data may be created in either text or binary protocols; The binary
# protocol is more efficient but it cannot be readily understood if inspected;
# By default, storage protocol in python 3 is binary bytes format (protocol = 3);
# Text format - human readable ASCII format (protocol = 0)

print(pickle.dumps([1, 2, 3]))  # Default protocol is 3
print(pickle.dumps([1, 2, 3], protocol=0))

# To store/dump onto a database, applying protocol=0 will produce
# TypeError: must be str, not bytes; But for parsing for bytes streaming
# or buffering io.bytesIO works

B = io.BytesIO()
pickle.dump([1, 2, 3], B)
print(B.getvalue())

# Resetting io.BytesIO, B, each time.
B = io.BytesIO()
pickle.dump([1, 2, 3], B, protocol=0)
print(B.getvalue())


