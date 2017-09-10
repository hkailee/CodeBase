#!/usr/local/bin/python3

"""
Not much of a new topic compared to dbm and pickle earlier, simply using
DBM and object pickling internally, but with several advantages to retrive big dataset
(i.e. Analogy of a shelf storing multiple DBM files indexed by keys for retrieval):
1. To store an in-memory object by key, the shelve module first serializes the
object to a string with the pickle module, and then it stores that string in a
DBM file by key with the dbm module.
2.To fetch an object back by key, the shelve module first loads the object’s
serialized string by key from a DBM file with the dbm module, and then converts
it back to the original in-memory object with the pickle module.

Limitation:
1. keys must be string, i.e not number etc
2. Objects are unique only within a key
3. Updates must treat shelves as fetch-modify-store mappings
4. Concurrent updates are not directly supported
5. Underlying DBM format portability (i.e. gdbm on Linux not compatible with
   bsddb on Windows) - Use the OODB (ZODB) system if this is a concern.
"""

import shelve

# Create new database
dbase = shelve.open('mydbase')
object1 = ['The', 'bright', ('side', 'of'), ['life']]
object2 = {'name': 'Brian', 'age': 33, 'motto': object1}

dbase['brian'] = object2
dbase['knight'] = {'name':'Knight', 'motto': 'Ni!'}
dbase.close()

# loading existing database, mydbase
dbase = shelve.open('mydbase')
print(len(dbase))
print(list(dbase.keys()))
print(dbase['knight'])      # fetch
for row in dbase.keys():
    print(row, '=>')
    for field in dbase[row].keys():
        print('    ', field, '=', dbase[row][field])

# How about storing class instance?
class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job
        self.pay = pay          # real instance data
    def tax(self):
        return self.pay * 0.07
    def info(self):
        return self.name, self.job, self.pay, self.tax()

bob = Person('bob', 'psychologist', 70000)
emily = Person('emily', 'teacher', 40000)

dbase = shelve.open('cast')     # make new shelve
for obj in (bob, emily):
    dbase[obj.name] = obj

dbase.close()

# Reopen the shelve of class instance
dbase = shelve.open('cast')     # reopen shelve
print(list(dbase.keys()))
print(dbase['emily'].tax())     # call: emily's tax