#solution_python2_chapter06_database_tests.py

"""This unittest file can be used with different database,
   table, and file names to test against different configurations.
   Here, we simply use the same ones as the tested file does.
"""

import unittest
import sqlite3
from  solution_python2_chapter06_database import \
      create_database, get_nh_results_nl_after_june

DB='db'
TABLE='baseball'
FILE='py_baseball_data.csv'

class Tester(unittest.TestCase):
    def setUp(self):
        #create the database
        create_database(db=DB, table=TABLE, file=FILE)
        #provide the test class its own connection and cursor
        self.conn = sqlite3.connect (DB)
        self.curs = self.conn.cursor() 
        
    def test_count(self):
        "there should be four matchers"
        results=get_nh_results_nl_after_june(db=DB, table=TABLE)
        self.assertEqual(len(results), 4)
        
    def test_record(self):
        """there should be a matching record something like:
          2015, 8, 30, 'Arrieta', ' Jake', 'Chicago', 'NL'
          ... so is it really there?"""
        results=get_nh_results_nl_after_june(db=DB, table=TABLE)
        for row in results:
            year, month, day, last, first, team, league = row
            #check for the right day
            if year==2015 and month==8 and day==30:  
                #... on that day, can we find Arrieta?
                self.assertEqual(last.strip(), 'Arrieta')
                self.assertEqual(first.strip(), 'Jake')
                self.assertEqual(team.strip(), 'Chicago')
                self.assertEqual(league.strip(), 'NL')
                
    def tearDown(self):
        cmd = "DROP TABLE IF EXISTS {}".format(TABLE)
        self.curs.execute(cmd)
        pass
    
if __name__=='__main__':
    unittest.main()