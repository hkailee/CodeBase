#!/usr/local/bin/python3

'''
More advanced script pls refer to loaddb.py
'''


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

# Using special aggregate functions available from sql
curs.execute("select sum(pay), avg(pay) from people where job = 'devel'")
print(curs.fetchall())

# Or computing pay sums and averages with Python can be accomplished with a simple loop
curs.execute("select name, pay from people where job = 'devel'")
result = curs.fetchall()
print(result)

tot = 0
for (name, pay) in result:
    tot += pay
print('total:', tot, 'average:', tot / len(result))

print(sum(rec[1] for rec in result))
print(sum(rec[1] for rec in result) / len(result))
print(max(rec[1] for rec in result))

avg = sum(rec[1] for rec in result) / len(result)
print([rec[0] for rec in result if rec[1] > avg])
print([rec[0] for rec in result if rec[1] < avg])

# Using sql command to look for specific data
query = ("select name from people where job = 'devel' and "
            "pay > (select avg(pay) from people where job = 'devel')")
curs.execute(query)
print(curs.fetchall())


conn.commit()
