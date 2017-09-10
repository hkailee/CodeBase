#!/usr/local/bin/python3

"""
pickle to/from flat file utilities
"""

import pickle

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
