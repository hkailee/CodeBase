#!/usr/local/bin/python3

"""
the connect call’s arguments are usually the only thing that can vary across
different database systems. For example, in the MySQL interface this call accepts
a network host’s domain name, user name, and password, passed as keyword
arguments instead, and the Oracle example sketched earlier expects a more specific
string syntax. Once we’ve gotten past this platform- specific call, though,
the rest of the API is largely database neutral.
"""

import sqlite3

# Create new database (Kind of Boilerplate code)
conn = sqlite3.connect('dbase_Sqlite')

curs = conn.cursor()
tblcmd = 'create table people (name char(30), job char(10), pay int(4))'
curs.execute(tblcmd)

# To insert data
print(sqlite3.paramstyle)  # this returns "qmark" tells this module accepts ? for replacement targets

curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
print(curs.rowcount)

curs.executemany('insert into people values (?, ?, ?)',
                 [ ('Sue', 'mus', '70000'),
                   ('Ann', 'mus', '60000')])

print(curs.rowcount)

rows = [['Tom', 'mgr', 100000],
        ['Kim', 'adm', 30000],
        ['pat', 'dev', 90000]]


for row in rows:
    curs.execute('insert into people values (? , ?, ?)', row)

# Without a commit, a connection rollback or close call, as well as the
# connection’s __del__ deletion method, will back out uncommitted changes.
conn.commit()

# Different styles to  view data
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)

curs.execute('select * from people')
for (name, job, pay) in curs.fetchall():
    print(name, ':', pay)

curs.execute('select name from people')
names = curs.fetchall()
print(names)

curs.execute('select * from people')
names = [rec[0] for rec in curs.fetchall()]
print(names)

curs.execute('select * from people')
while True:
    row = curs.fetchone()
    if not row:
        break
    print(row)

curs.execute('select * from people')
while True:
    rows = curs.fetchmany()  # size=N optional argument
    if not row:
        break
    for row in rows:
        print(row)

curs.execute('select name, job from people where pay > 60000')
print(curs.fetchall())

query = 'select name, job from people where pay >= ? order by name'
curs.execute(query, [60000])
for row in curs.fetchall():
    print(row)

# Update a record
curs.execute('update people set pay=? where pay <= ?', [65000, 60000])
print(curs.rowcount)
curs.execute('select * from people')
print(curs.fetchall())

# To delete a record
curs.execute('delete from people where name = ?', ['Bob'])
curs.execute('delete from people where pay >= ?',(90000,))
curs.execute('select * from people')
print(curs.fetchall())

conn.commit()
conn.close()