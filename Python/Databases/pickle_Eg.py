#!/usr/local/bin/python3

"""
super general data formatting and de-formatting tool—pickle converts nearly
arbitrary Python in-memory objects to and from a single linear string format,
suitable for storing in flat files, shipping across network sockets between
trusted sources, and so on. This conversion from object to string is often
called serialization—arbitrary data structures in memory are mapped to a
serial string form; Pickling works on almost any Python datatype—numbers,
lists, dictionaries, class in- stances, nested structures, and more—and so
is a general way to store data.
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







