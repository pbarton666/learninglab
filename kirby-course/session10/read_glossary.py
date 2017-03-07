# -*- coding: utf-8 -*-
"""
Created on Aug  4, 2016
Modified Mon Dec 12, 2016

@author: Kirby Urner

Fills an SQL database from a text file: glossary.txt

----
* .NET:  a virtual machine and the target runtime platform ...

* Agile:  a set of practices and work flows designed to promote ...

* AJAX:  asynchronous JavaScript and XML.  Loosely describes ...

* Apache:  a free / open source web server, highly configurable ...
-----

sqlite> SELECT gl_term FROM glossary ORDER by gl_term COLLATE NOCASE;
.NET:
Agile:
AJAX:
Apache:
Apache Foundation:
...

sqlite> select gl_definition from glossary where gl_term = "Tk";
a GUI tool kit, written in tcl.
"""

import sqlite3 as sql
import time
import os

FILE = "glossary.txt"  # adjust as needed

class DB:

    backend  = 'sqlite3'
    user_initials  = 'KTU'
    timezone = int(time.strftime("%z", time.localtime()))
    target_path = os.getcwd()  # current directory
    db_name = os.path.join(target_path, 'glossary.db')

    @staticmethod
    def mod_date():
        return time.mktime(time.gmtime())  # GMT time

    @classmethod
    def connect(cls):
        try:
            if cls.backend == 'sqlite3':
                cls.conn = sql.connect(DB.db_name)
                cls.c = cls.conn.cursor()
            elif cls.backend == 'mysql':
                cls.conn = sql.connect(host='localhost',
                                      user='root', port='8889')
                cls.c = cls.conn.cursor()
        except:
            raise

    @classmethod
    def disconnect(cls):
        if cls.conn:
            cls.conn.close()

    @classmethod
    def save_term(cls, *the_data):
        query = ("INSERT INTO Glossary "
        "(gl_term, gl_definition, updated_at, updated_by) "
        "VALUES ('{}', '{}', {}, '{}')".format(*the_data))
        # print(query)
        cls.c.execute(query)
        cls.conn.commit()

    @classmethod
    def create_table(cls):
    
        # https://www.sqlite.org/lang_droptable.html
        cls.c.execute("""DROP TABLE IF EXISTS Glossary""")
        cls.c.execute("""CREATE TABLE Glossary
            (gl_term text PRIMARY KEY,
             gl_definition text,
             updated_at int,
             updated_by text)""")
             
class DBcontext:

    def __enter__(self):
        DB.connect()
        return DB

    def __exit__(self, *stuff_happens):
        DB.disconnect()
        if stuff_happens[0]:
            print(stuff_happens)
            return False
        return True

with DBcontext() as dbx:

    dbx.create_table()

    with open(FILE, 'r', encoding='UTF-8') as gloss:
        lines = gloss.readlines()

    for line in lines:
        if len(line.strip()) == 0:  # skip blank lines
            continue
        term, definition = line.split(":", 1)
        right_now = dbx.mod_date()
        dbx.save_term(term[2:].strip(), definition.strip(), 
                     right_now, dbx.user_initials)

print("Done!")