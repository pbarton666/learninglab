
#solution_python2_chapter07_logging.py

import sqlite3
import csv     #python's library for reading csv files
import logging

DB='beer'
TABLE='brewpub'
FILE='py_log_english_brewery_data.csv'
LOG_FILE='brewery.log'
LEVEL=logging.DEBUG

logging.basicConfig(filename=LOG_FILE, 
                    level=LEVEL)
logger=logging.getLogger()

def create_database(db=DB, table=TABLE, file=FILE):
    "Creates a database w/ table loaded with file data"
    #connect to the database
    logger.debug("connecting to database")
    conn = sqlite3.connect (DB)
    curs = conn.cursor()
    
    #set up a data table
    logger.debug("setting up the {} table".format(TABLE)) 
    curs.execute("DROP TABLE IF EXISTS {}".format(TABLE))
    cmd = """CREATE TABLE {}
                         (name   TEXT(50), 
                          is_ale TINYINT,
                          county TEXT(50)
                          )""".format(TABLE)
    curs.execute(cmd)
    conn.commit()

    #Keeping it DRY, introspect for column names    
    cmd = "SELECT * FROM {}".format(TABLE)
    curs.execute(cmd)    
    cols=[]
    for name in curs.description:
        cols.append(name[0])
    cols=tuple(cols)
    
    #create a master set of info collected from data file
    master=set()
    
    #open the file and read it, dropping each row into the data table
    logger.debug("opening {}".format(FILE))
    with open(FILE, 'r') as data_file:
        reader=csv.reader(data_file)
        next(reader) #skips the header row
        for data in reader:
            #Each row is a list of strings.  Clean them up a bit.
            name, county = data
            name=name.strip()
            county=county.strip()
            is_ale=0
            if "ale" in name.lower():
                is_ale=1
            #create a tuple for input to INSERT
            master.add( (name, is_ale, county) )
            
    #At this point, the master set of info is deduped, so
    #  add its contents to the database.  Note that we could
    #  add everything to the database then grab unique values
    #  via a SELECT DISTINCT directive.
    for item_tuple in master:    
        cmd= "INSERT INTO {} {} VALUES {}".format(
              TABLE, cols, item_tuple)
        curs.execute(cmd)
    logger.debug("making commits to the {} table".format(TABLE))
    conn.commit()
    conn.close()

def get_ale_houses(db=DB, table=TABLE, is_ale=1, county=0): 
    "finds places based on whether they do ale and their location"
    logger.debug("Finding ale houses in {}.".format(TABLE))
    conn = sqlite3.connect (DB)
    curs = conn.cursor()    
    if not county:  
        cmd="SELECT * FROM {} WHERE is_ale={}".format(TABLE, is_ale)
    else:
        cmd="SELECT * FROM {} WHERE is_ale={} AND county='{}'"\
            .format(TABLE, is_ale, county)
    curs.execute(cmd)
    results=curs.fetchall()
    logger.debug("... found {} ale houses!".format(len(results)))
    return results

if __name__=='__main__':
    create_database()
    results=get_ale_houses()
    print(results)

        
    