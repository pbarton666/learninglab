#py_sql_1.py

#import the python/sqlite3 connector;  
#...there are others for postgresql, mysql, etc.
import sqlite3

#create a connection object (on other RMDBs you'd provide credentials, too)
conn = sqlite3.connect('mydb')

#creates a cursor object
curs = conn.cursor()

#SQL is case-insensitive, but most people use CAPS for keywords

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

#get some results
cmd = "SELECT * from {}".format('dogs')
print(cmd)
curs.execute(cmd)
result=curs.fetchall()
print(result)

#... and print them out (if there are any)
if result:
    print("congrats, you've got some dawgs")
    for row in result:
        name, toy, weight=row
        print(name, toy, weight)
        
#Here's an alternative way to insert rows
curs.executemany('INSERT INTO dogs VALUES(?,?,?)',
                 [('Biscuit', 'towel', '70'),
                  ('Snoopy', 'squirrel', '60')
                 ]
                 )
        
#It may make sense to create names for the table and its columns              
cols=('name', 'toy','weight')
tname='dogs'
val_tuple=("Fluffy", "sock", "25")

cmd=\
    "INSERT INTO {} {} VALUES (?, ?, ?) ".format(tname, cols)

curs.execute(cmd, val_tuple)
print()

#with names we can simply recycle them
def print_rows():
    "a utility function you may want to keep"
    cmd = "SELECT * from {}".format(tname)
    print(cmd)
    curs.execute(cmd)
    result=curs.fetchall()
    if result:
        for r in result:
            nice_output=''
            for label, res in zip(cols, r):
                nice_output+="{:>10} = {:<10}".format(label, res)
            print (nice_output)

print_rows()

#Getting column names from the database
curs.execute(cmd)
for ix, name in enumerate(curs.description):
    print("column {} is called {}".format(ix, name[0]))


#Figure out how many rows in the table
cmd="SELECT COUNT(*) FROM {}".format(tname)
curs.execute(cmd)
result=curs.fetchone()
number_of_rows, = result   
print("Awesome, we've captured {} rows.".format (number_of_rows))

print()

#Retrieving information
#

#Ask for everything:
curs.execute('SELECT * FROM dogs')

#You can get however many results using fetchone(), fetchall() or fetchmany()
curs.execute('SELECT * FROM dogs')
while True:
    row = curs.fetchone()
    if not row:
        break
    print(row)
print('*'*20)

curs.execute('SELECT * FROM dogs')
while True:
    row = curs.fetchmany(2)
    if not row:
        break
    print(row)
print('*'*20)

#You can make queries as complex/fancy as you want    
cmd = 'SELECT name, weight FROM dogs WHERE weight >= 60'
print(cmd)
curs.execute(cmd)
print(curs.fetchall())

#... and order the results
cmd = 'SELECT name, weight FROM dogs WHERE weight >= 60 ORDER BY name'
print(cmd)
curs.execute(cmd)
print_rows()

for row in curs.fetchall():
    print(row)
print(curs.fetchall())


#updates
print()
cmd="UPDATE {} SET weight=? WHERE name='Snoopy'".format(tname)
weight=(666,)
curs.execute(cmd, weight)

cmd="SELECT * FROM {} WHERE name='Snoopy'".format(tname)
print(cmd)
curs.execute(cmd)
result=curs.fetchone()
print(result)

#deletions

cmd= "DELETE FROM {} WHERE toy = ? ".format(tname)
toy = ('sock',)
curs.execute(cmd, toy)
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()

cmd= "DELETE FROM {} WHERE toy LIKE ?".format(tname)
toy_selector = ('%el',)
curs.execute(cmd, toy_selector)
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()


cmd= "DELETE FROM {}".format(tname)
curs.execute(cmd)
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()
