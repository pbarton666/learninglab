# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:30:15 2017

@author: kurner
"""

import unittest
import requests
import unittest.mock
import os

# inside application subfolder
os.chdir("/Users/kurner/Downloads/session10/coasters")

from make_coasters_db import DB

HOST = 'http://localhost:5000'

class Coasters(unittest.TestCase):
    
    def setUp(self):
        self.requests = unittest.mock.MagicMock(spec=requests)
        obj = unittest.mock.Mock()
        obj.status_code = 200
        obj.text = ''
        self.requests.get.return_value = obj
    
    def test_get_coaster(self):
        r = self.requests.get(HOST)
        self.assertEqual(r.status_code, 200)
            
    def test_unreal(self):
        pass
        
def realDB():
    with DB() as db:
        coaster = "Volcano%"
        query = ("SELECT * FROM Coasters "
                 "WHERE name LIKE '{}'".format(coaster)) 
        print(query)
        db.get_coasters(query)
        results = tuple(db.cursor.fetchall())
    return results
    
def realWeb():
    r = requests.get(HOST)
    print("Status:", r.status_code)
    r = requests.get(HOST + "/coasters")
    print("Returned:", len(r.text))
    r = requests.get(HOST + "/coaster/X")
    print("Status:", r.status_code) 
    print("Headers: ", r.headers)    
    r = requests.get(HOST + "/api/coaster/X")
    print("Status:", r.status_code)
    print("Headers: ", r.headers)
    print("JSON:", r.text)  
     
    
if __name__ == "__main__":
    #unit tests
    # unittest.main()
    
    # integration tests
    realWeb()
    print(realDB())
    