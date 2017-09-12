#!/usr/local/bin/python3

"""
ORM maps
1. Python classes to database tables
2. Python class instances to rows in the table
3.  Python instance attributes to row columns
"""

from sqlobject import SQLObject, sqlhub, connectionForURI, StringCol

sqlhub.processConnection = connectionForURI('sqlite:/:memory:')

class Person(SQLObject):                    # class: describes table
    first = StringCol()                     # class attributes: row columns
    mid = StringCol(length=1, default=None)
    last = StringCol()

Person.createTable()                        # create a database table

p = Person(first='Bob', last='Smith')       # new instance: makes and inserts row
print(p)                                    # prints all attributes by name

print(p.first)                              # attribute: fetches row column
p.mid = 'M'                                 # attribute: updates record

p2 = Person.get(1)                          # fetch existing record/instance: p2 is p
print(p2)

p.set(first='Tom', last='Jones')            # update two attributes/fields at once
print(p)

ts = Person.select(Person.q.first=='Tom')       # query: select by column value
print(list(ts)) # run the query: list of instances
tjs = Person.selectBy(first='Tom', last='Jones') # alternative query form (AND)
print(tjs)