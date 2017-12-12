#py_sql_1.py

#import the python/sqlite3 connector;  
#...there are others for postgresql, mysql, etc.
import sqlite3

#create a connection object (on other RMDBs you'd provide credentials, too)
conn = sqlite3.connect('mydb')

#creates a cursor object
curs = conn.cursor()

#Here, we get rid of the table 'dogs' (IF EXISTS prevents a crash)
cmd = "DROP TABLE IF EXISTS dogs"
curs.execute(cmd)    #this runs the SQL command
conn.commit()        #... and this locks in the changes

#Build a new table's metadata (framework)
cmd = """CREATE TABLE dogs (name CHAR(10), 
                            toy CHAR(10), 
                            weight INT(4))"""
print(cmd)
curs.execute(cmd)

#add a row
cmd = "INSERT INTO dogs ('name', 'toy', 'weight') VALUES (?, ?, ?)"
vals= ('Fang', 'bone', 90)
curs.execute(cmd, vals)


cmd = "SELECT * from {}".format('dogs')
print(cmd)
curs.execute(cmd)
result=curs.fetchall()
print(result)

if result:
    print("congrats, you've got some dawgs")
    for row in result:
        name, toy, weight=row
        print(name, toy, weight)
        
