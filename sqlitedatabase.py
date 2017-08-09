# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 21:29:23 2017

@author: 310247467
"""

import sqlite3

def ConnectAndCreate():
    try:
        conn=sqlite3.connect('data.db')
    except sqlite3.Error:
        try:
            conn.execute('''CREATE TABLE IF NOT EXITS LIST
             (ID VARCHAR PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL);''')
        except sqlite3.Error:
            return conn
        
        return conn
    try:
        conn.execute('''CREATE TABLE LIST
             (ID VARCHAR PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL);''')
    except sqlite3.Error:
        return conn
    conn.commit()
    return conn

def LoadFromDatabase(dictionarylist,conn):
    cursor=conn.execute('''select * from LIST''')
    for row in cursor:
        dictionarylist[row[0]]=row[1]
    return dictionarylist

def LoadToDatabase(conn,itemlist):
    for item in itemlist:
        conn.execute('insert into LIST values (?,?)', item)