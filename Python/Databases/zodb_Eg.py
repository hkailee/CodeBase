#!/usr/local/bin/python3

"""
Zope Object Database (ZODB) - An Object-oriented Database (OODB)
Compared to shelve, this supports:
1. immediate auto write-through on changes,
2. transaction commits and rollbacks,
3. safe concurrent updates
4. object decomposition and delayed ('lazy') component fetches based on generated
object IDs
"""

from ZODB import FileStorage, DB

# Create new database
dbase = FileStorage.FileStorage('mydbase')


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