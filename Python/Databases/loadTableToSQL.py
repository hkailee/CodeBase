#!/usr/local/bin/python3

# For MySQL

# conn = connect('dbase')             # Connect with user and password
# curs = conn.cursor()
#
# curs.execute("delete from people")  # delete all records
# curs.execute("LOAD data local infile 'data.txt' into table people fields terminated by ','")
#
# curs.execute('select * from people')
# for row in curs.fetchall():
#     print(row)
#
# conn.commit() # save inserted records


# For sqlite3
from sqlite3 import connect
conn = connect('dbase_Sqlite')
curs = conn.cursor()
curs.execute('delete from people')
curs.execute('select * from people')
print(curs.fetchall())          # table should be empty by now

file = open('data.txt')
rows = [line.rstrip().split(',') for line in file]
print(rows[0])

for rec in rows:
    curs.execute('insert into people values (?, ?, ?)', rec)

curs.execute('select * from people')
for rec in curs.fetchall():
    print(rec)

conn.commit()
