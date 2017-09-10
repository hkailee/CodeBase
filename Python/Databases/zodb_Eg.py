#!/usr/local/bin/python3

"""
Zope Object Database (ZODB) - An Object-oriented Database (OODB)
Compared to shelve, this supports:
1. immediate auto write-through on changes,
2. transaction commits and rollbacks,
3. safe concurrent updates
4. object decomposition and delayed ('lazy') component fetches based on generated
object IDs
5. Automatic caching of objects
6. compatible with all the platforms (i.e. windows and linux).

Limitations:

1. Accessing the database requires a small amount of extra boilerplate code to
interface with ZODB—it’s not a simple open call.
2. Classes are derived from a persistence superclass if you want them to take
advantage of automatic updates on changes—persistent classes are generally not
as completely independent of the database as in shelves, though they can be.

Alternative to ZODB is Dulus
"""

from ZODB import FileStorage, DB
import transaction
from persistent import Persistent

# Create new database (Kind of Boilerplate code)
storage = FileStorage.FileStorage('mydb.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

object1 = (1, 'spam', 4, 'you')
object2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
object3 = {'name': ['Bob', 'Doe'], 'age': 42, 'job': ('dev', 'mgr')}

root['mystr'] = 'spam' * 3
root['mytuple'] = object1
root['mylist'] = object2
root['mydict'] = object3

print(root['mylist'])

# transaction rollbacks, must commit your changes to the database to make
# them permanent. Without the final commit in this session, none of the
# changes we made would be saved.

transaction.commit()
storage.close()

# To load the existing database (Similar to creating anew)
storage = FileStorage.FileStorage('mydb.fs')
db = DB(storage)
connection = db.open()
root = connection.root()        # make connect

print(len(root), root.keys())
print(root['mylist'])
print(root['mydict'])
print(root['mydict']['name'][-1])

for key in root.keys():
    print('%s => %s' % (key.ljust(10), root[key]))

# How about storage and retrieval of class instance objects;
# and making use of persistent.Persistent to automatically flush
# changes to disk

class Person(Persistent):
    def __init__(self, name, job=None, rate=0):
        self.name = name
        self.job = job
        self.rate = rate
    def changeRate(self, newrate):
        self.rate = newrate         # automatically update database

root['Bob'] = Person('Kai', "Senior Research Fellow", 100000)
root['Bob'].changeRate(120000)
print(root['Bob'].rate)