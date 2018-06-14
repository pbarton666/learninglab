#py_sql_injection.py

"""Many thanks to Steve Holden"""

import sqlite3

#create connector and cursor intances
print("establishing connector and cursor", end=" ... ")
conn = sqlite3.connect('dbase1')
curs = conn.cursor()
print("done")

#clear any existing table 'dogs'
print("dropping table dogs", end=" ... ")
curs.execute("DROP TABLE IF EXISTS dogs")  
conn.commit()        
print("done")

#Build a new 'dogs' table
print("building new table dogs", end=" ... ")
cmd = """CREATE TABLE dogs (name CHAR(10), 
                            toy CHAR(10), 
                            weight INT(4))"""
curs.execute(cmd)
print("done")

#add some dogs using a raw Python string
print("adding some dogs to the table", end=" ... ")
stg = \
"""
INSERT INTO dogs ({}, {}, {}) 
            VALUES ('{}','{}','{}')
"""

curs.execute(stg.format('name', 'toy', 'weight', "Fang",  "bone",     70))
curs.execute(stg.format('name', 'toy', 'weight', "Sara",  "squeaker", 40))
curs.execute(stg.format('name', 'toy', 'weight', "Quinn", "bunny",    90))
conn.commit()
print("done\n")

#check out the contents
cmd="SELECT * from dogs"
curs.execute(cmd)
for row in curs.fetchall():
    print(row)

#Now the injection attack:
print("injecting malicious code", end=" ... ")
#   SELECT * FROM dogs WHERE name='Diablo;
#   DROP TABLE dogs;
#   <this bit is a SQL comment> =='

cmd = "SELECT * from dogs WHERE name='Diablo'; DROP TABLE dogs;--'"
curs.executescript(cmd)
print("done")

print()
print ('trying to get table "dogs"', end=" ... ")
print()
try:
    cmd="SELECT * from dogs"
    curs.execute(cmd)
except Exception as e:
    print(e)

#=============================================
#  Much safer:
#=============================================

#Build a new 'dogs' table
print("building new table dogs", end=" ... ")
cmd = """CREATE TABLE dogs (name CHAR(10), 
                            toy CHAR(10), 
                            weight INT(4))"""
curs.execute(cmd)
print("done")

#add some dogs using a sqlite3 escape
print("adding some dogs to the table", end=" ... ")
stg = \
"""
INSERT INTO dogs ({}, {}, {}) 
            VALUES (?, ?, ?)
"""

#this uses format() for the names and passes a tuple to replace "?"
print("adding new dogs", end = " ... ")
curs.execute(stg.format('name', 'toy', 'weight'), ("Fang",   "bone",      70) ) 
curs.execute(stg.format('name', 'toy', 'weight'),  ("Sara",  "squeaker",  40))
curs.execute(stg.format('name', 'toy', 'weight'), ("Quinn",  "bunny",     90))
conn.commit()
print("done\n")

#Now the injection attack:
print("injecting malicious code", end=" ... ")
name = "'Diablo'; DROP TABLE dogs;--'"
cmd = "SELECT * from dogs WHERE name= ?; DROP TABLE dogs;--'"
try:
    curs.executescript(cmd, (name,))
except Exception as e:
    print(e)
    
print("done injecting")

print()
print ('trying to get table "dogs"', end=" ... ")
print()
try:
    cmd="SELECT * from dogs"
    curs.execute(cmd)
    for dawg in curs.fetchall():
        print(dawg)
except Exception as e:
    print(e)