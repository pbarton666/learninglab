
#solution_python2_chapter06_database.py

import sqlite3
import csv     #python's library for reading csv files

DB='db'
TABLE='baseball'
FILE='py_baseball_data.csv'

def create_database(db=DB, table=TABLE, file=FILE):
    "Creates a database w/ table loaded with file data"
    #connect to the database
    conn = sqlite3.connect (DB)
    curs = conn.cursor()
    
    #set up a data table
    cmd = "DROP TABLE IF EXISTS {}".format(TABLE)
    curs.execute(cmd)
    
    cmd = """CREATE TABLE {}
                         (year   INT, 
                          month  INT, 
                          day    INT, 
                          last   TEXT(20), 
                          first  TEXT(20), 
                          team   TEXT(30), 
                          league TEXT(2)
                          )""".format(TABLE)
    curs.execute(cmd)
    conn.commit()

    #Keeping with DRY (don't repeat yourself), we'll grab the column
    #  names we just added.  Then provide a handle to them.  We can
    #  convert them for a tuple to feed to the INSERT statement below
    
    cmd = "SELECT * FROM {}".format(TABLE)
    curs.execute(cmd)
    
    cols=[]
    for name in curs.description:
        cols.append(name[0])
    cols=tuple(cols)
    
    #open the file and read it, dropping each row into the data table 
    with open(FILE, 'r') as data_file:
        reader=csv.reader(data_file)
        next(reader) #skips the header row
        for data in reader:
            #create tuples for our data and column values
            cmd= "INSERT INTO {} {} VALUES {}".format(
                  TABLE, cols, tuple(data))
            curs.execute(cmd)
    conn.commit()
    conn.close()

def get_nh_results_nl_after_june(db=DB, table=TABLE): 
    "dig out the ho-hitters after June by NL teams"
    conn = sqlite3.connect (DB)
    curs = conn.cursor()    
    cmd="SELECT * FROM {} WHERE league='NL' AND month>6".format(TABLE)
    curs.execute(cmd)
    
    results=curs.fetchall()
    return results

if __name__=='__main__':
    create_database()
    results=get_nh_results_nl_after_june()
    print(results)

        
    