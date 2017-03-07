#py_sql_1

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
cmd = \
"""
INSERT INTO dogs ({}, {}, {}) 
            VALUES ('{}','{}','{}')
"""\
       .format('name', 'toy', 'weight', "Fang", "bone", 90) 
print(cmd)
curs.execute(cmd)


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
        

        
              
cols=('name', 'toy','weight')
tname='dogs'
val_tuple=("Fluffy", "sock", "25")
cmd=\
    """INSERT INTO {} {} \nVALUES {} """\
    .format(tname, cols, val_tuple)
print(cmd)
curs.execute(cmd)
print()

def print_rows():
    cmd = "SELECT * from {}".format('dogs')
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

curs.executemany('INSERT INTO dogs VALUES(?,?,?)',
                 [('Biscuit', 'towel', '70'),
                  ('Snoopy', 'squirrel', '60')
                 ]
                 )
print_rows()

cmd = "SELECT * from {}".format('dogs')
print(cmd)
curs.execute(cmd)
result=curs.fetchall()
if result:
    for r in result:
        nice_output=''
        for label, res in zip(cols, r):
            nice_output+="{:>10} = {:<10}".format(label, res)
        print (nice_output)

#

#Here's how to get values out.  This has the effect of loading
#  up the cursor object with results.  But evaluation is 'lazy'
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

q = 'SELECT name, weight FROM dogs WHERE \
     weight > 100 ORDER BY name'

cmd="SELECT * FROM {}".format(tname)
curs.execute(cmd)
for ix, name in enumerate(curs.description):
    print("column {} is called {}".format(ix, name[0]))

cmd="SELECT COUNT(*) FROM {}".format(tname)
curs.execute(cmd)
result=curs.fetchone()
number_of_rows, = result   
print("Awesome, we've captured {} rows.".format (number_of_rows))


#updates
print()
cmd="UPDATE {} SET weight=666 WHERE name='Snoopy'".format(tname)
print(cmd)
curs.execute(cmd)
cmd="SELECT * FROM {} WHERE name='Snoopy'".format(tname)
print(cmd)
curs.execute(cmd)
result=curs.fetchone()
print(result)


print()
print("Dog Table")
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()


cmd= "DELETE FROM {} WHERE toy = 'sock'".format(tname)
curs.execute(cmd)
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()

cmd= "DELETE FROM {} WHERE toy LIKE '%el'".format(tname)
curs.execute(cmd)
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()


cmd= "DELETE FROM {}".format(tname)
curs.execute(cmd)
cmd = "SELECT * FROM {}".format(tname)
curs.execute(cmd)
print_rows()
a=1