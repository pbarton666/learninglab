# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:58:06 2017
Modified Mar 21, 2017 to send a pull request to pbarton.

This DB class does not yet implement full "CRUD" i.e.
it creates the coaster table, inserts new coasters,
but does not delete or update existing coaster records.
For this Flask application to be more complete as a
demo, we need delete and update. I am adding stubs 
in this commit.

@author: Kirby Urner
@co-author: Patrick Barton

Consumes csv data put into a dictionary by rollercoasters.py
Creates a SQL_Lite DB and inserts the data.
"""

import os
import sqlite3 as sql

class DB:

    target_path = os.getcwd()  # current directory
    db_name = os.path.join(target_path, 'roller_coasters.db')

    @classmethod
    def __enter__(cls):
        print("running enter")
        cls.conn = sql.connect(DB.db_name)
        cls.cursor = cls.conn.cursor()
        return cls
        
    @classmethod
    def __exit__(cls, *oops):
        print("running exit")
        print(oops)
        cls.conn.close()

    @classmethod
    def zap_table(cls):
        # https://www.sqlite.org/lang_droptable.html
        cls.cursor.execute("""DROP TABLE IF EXISTS Coasters""")

    @classmethod
    def create_table(cls):
        cls.cursor.execute("""CREATE TABLE Coasters
            (Name text PRIMARY KEY, 
             Park text,
             State text, 
             Country text,
             Duration int,
             Speed int,
             Height int,
             VertDrop int,
             Length int,
             Yr_Opened int,
             Inversions int)""")
     
    @classmethod
    def update_coaster(cls, row): # use primary key
        "this allows user to update coaster properties"
        
        #invoked from coaster_app.py::coaster() by dint of SUBMIT
        #  button defined in coaster.html
        print("Updating...")
        print("Raw data:",row)
        col_names= ('Park', 'State', 'Country', 'Duration', 'Speed', 'Height', 
        'VertDrop', 'Length', 'Yr_Opened', 'Inversions')
        
        sql = (",\n".join(("UPDATE Coasters SET "
                 "Park = '{Park}'",
                 "State = '{State}'",
                 "Country = '{Country}'",
                 "Duration = {Duration}",
                 "Speed = {Speed}",
                 "Height = {Height}",
                 "VertDrop = {VertDrop}",
                 "Length = {Length}",
                 "Yr_Opened = {Yr_Opened}",
                 "Inversions = {Inversions}")).format(**row))
                
        sql += " WHERE Name = '{}'".format(row['Name'])
        try:
            cls.cursor.execute(sql)
            cls.conn.commit() 
        except:
            print("SQL {} is not valid.  Sorry, dude.".format(sql))
    
    @classmethod
    def delete_coaster(cls, coaster): # use primary 
        """
        get the coaster by name, and delete it
        """
        if "'" in coaster:
            coaster = coaster.replace("'", "''")
        if "," in coaster:
            coaster = coaster.replace(",", "%")
            coaster=coaster[:coaster.index('%')+1]
        if "%" not in coaster:
            query = ("DELETE FROM Coasters "
                     "WHERE name = '{}'".format(coaster))
        else:
            query = ("DELETE FROM Coasters "
                     "WHERE name LIKE '{}'".format(coaster))
        cls.cursor.execute(query)
        cls.conn.commit()        
    
    @classmethod
    def save_coaster(cls, row):
        # row should be tuple / namedtuple
        query = ("INSERT INTO Coasters "
        "('Name', 'Park', 'State', 'Country', 'Duration', 'Speed'," 
        " 'Height', 'VertDrop', 'Length', 'Yr_Opened', 'Inversions')"
        " VALUES ('{}', '{}', '{}', '{}', "
        "{}, {}, {}, {}, {}, {}, {})").format
        #print(query(*row))
        cls.cursor.execute(query(*row))
        cls.conn.commit()
        
    @classmethod
    def get_coasters(cls, the_query):
        cls.cursor.execute(the_query)

if __name__ == "__main__":
    import rollercoasters # don't need this if importing
    the_data = rollercoasters.read_csv()
            
    with DB() as db:
        db.zap_table()
        db.create_table()
        for rec in the_data.values():
            try:
                db.save_coaster(rec)
            except sql.OperationalError:
                print(rec)
            
    with DB() as db:
        query = ("SELECT name, park, yr_opened FROM Coasters "
                 "WHERE country = 'USA' ORDER BY Yr_Opened")
        db.get_coasters(query)
        results = []
        for rec in db.cursor.fetchall():
            results.append(rec)
    
    for row in results:
        print("{:25} {:35} {:4}".format(*row))

    
