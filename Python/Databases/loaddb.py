#!/usr/local/bin/python3

"""
load table from comma-delimited text file: reusable/generalized version Importable functions;
command-line usage: loaddb.py dbfile? datafile? table?
"""

import sqlite3


def login(dbfile):
    conn = sqlite3.connect(dbfile)  # create or open db file
    curs = conn.cursor()
    return conn, curs

def loaddb(curs, table, datafile, conn=None, verbose=True):
    file = open(datafile)                               # x,x,x\nx,x,x\n
    rows = [line.rstrip().split(',') for line in file]  # [[x,x,x], [x,x,x]]
    rows = [str(tuple(rec)) for rec in rows]            # ["(x,x,x)", "(x,x,x)"]
    for recstr in rows:
        curs.execute('insert into ' + table + ' values ' + recstr)
    if conn:
        conn.commit()
    if verbose:
        print(len(rows), 'rows loaded')