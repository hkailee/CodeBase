#!/usr/local/bin/python3

"""
pickle to/from flat file utilities
"""

import pickle

def saveDbase(filename, object):
    'save object to file'
    file = open(filename, 'wb')
    pickle.dump(object, file)
    file.close()

def loadDbase(filename):
    'load object from file'
    file = open(filename, 'rb')
    object = pickle.load(file)
    file.close()
    return object

L = [0]
D = {'x':0, 'y':L}
table = {'A': L, 'B': D}
saveDbase('myfile', table)
