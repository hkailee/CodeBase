'''
Be sure to also pass a string 'c' as a second argument when calling dbm.open to
force Python to create the file if it does not yet exist and to simply open it
for reads and writes otherwise. This used to be the default behavior but no
longer; Biggest weakness of DBM keyed files is in what they can store: data stored
under a key must be a simple string. If you want to store Python objects in a
DBM file, you can sometimes manually convert them to and from strings on writes
and reads (eg. str and eval calls); Not applicable for complex Python objects
such as class instances and nested data structures. Moreover, custom to-string
conversions and from-string parsers are error prone.
'''
import dbm

file = dbm.open('movie', 'c')
file['Batman'] = 'Pow!'

who = ['Robin', 'Cat-woman', 'Joker']
what = ['Bang!', 'Splat!', 'Wham!']
for i in range(len(who)):
    file[who[i]] = what[i]

print(file.keys())
print(file['Batman'])

for key in file.keys():
    print(key, file[key])

for key in file.keys():
    print(key.decode(), file[key].decode())

file['Batman'] = 'Ka-Boom!'
print(file['Batman'])

del file['Robin']

file.close()
