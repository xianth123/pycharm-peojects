#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('foot.db')
curs = conn.cursor()

curs.execute('''
CREATE  TABLE   food(
    id          TEXT       PRIMARY KEY,
    desc        TEXT,
    water       FLOAT,
    kcal        FLOAT,
    protein     FLOAT,
    fat         FLOAT,
    ash         FLOAT,
    carbs       FLOAT,
    fiber       FLOAT,
    sugar       FLOAT
)
 ''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:10]]
    print vals
    curs.execute(query, vals)

conn.commit()
conn.close()
