#!/usr/local/bin/python3

"""
Not much of a new topic compared to dbm and pickle earlier, simply a combination
of the DBM files and object pickling, but with several advantage for big dataset
(i.e. Analogy of a shelf storing multiple DBM files indexed by keys for retrieval):
1. To store an in-memory object by key, the shelve module first serializes the
object to a string with the pickle module, and then it stores that string in a
DBM file by key with the dbm module.
2.To fetch an object back by key, the shelve module first loads the object’s
serialized string by key from a DBM file with the dbm module, and then converts
it back to the original in-memory object with the pickle module.
"""

import pickle

# Create new database
table = {'a': [1, 2, 3],
         'b': ['spam', 'eggs'],
         'c': {'name':'bob'}}

mydb = open('dbase', 'wb')
pickle.dump(table, mydb)
mydb.close()

# Open existing database and unpickle it to show data
mydb = open('dbase', 'rb')
table = pickle.load(mydb)
print(table)

# Create database and unpickle
f = open('temp', 'wb')
x = ['Hello', ('pickle', 'world')]
pickle.dump(x, f)
f.close()

f = open('temp', 'rb')
y = pickle.load(f)
print(y)

print(x == y, x is y)







