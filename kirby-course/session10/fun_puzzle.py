# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16, 2016
Modified on Mon Dec 12, 2016

@author:Kirby Urner

A FUN PUZZLE IN PYTHON

Fun with testing

Our Animal has a stomach that may be fed, but not 
messed with from the outside, using dot notation.

__setattr__ gets used, not @property.  How do we 
initialize the _stomach to empty list then? 
 
Hint:  self.__dict__ has items, not attributes.
Rewriting line 29 will allow tests to pass.
"""

import unittest

class Animal:
    
    def __init__(self, nm = "Gordon"):
        self.name = nm
        # how do I initialize an empty stomach to begin with?
        self.__dict__['stomach'] = [] # this won't work
        
    def __call__(self, food):
        self.stomach.append(food)
        
    def __setattr__(self, the_attr, the_val):
        """
        if the_attr is 'stomach' we need to raise an AttributeError'
        Otherwise OK:
        """
        if the_attr == "stomach":
            raise AttributeError
        self.__dict__[the_attr] = the_val

class TestAnimal(unittest.TestCase):
    
    def test_problemo(self):
        obj = Animal("Roger")
        obj("juicy steak")
        obj("wine with cheese")
        obj("other condiments")
        self.assertRaises(AttributeError, obj.__setattr__, "stomach", 0)
        self.assertTrue(type(obj.stomach) == list)

    def test_attributes(self):
        obj = Animal("Roger")
        obj.fav_color = "orange"
        obj.age = 11
        self.assertEqual(obj.age, 11)
        self.assertEqual(obj.fav_color, "orange")
        
    def test_eating(self):
        obj = Animal("Roger")
        obj("spaghetti")
        self.assertEqual(obj.stomach, ['spaghetti'], "Problem!")        

if __name__ == "__main__":
    unittest.main()
    





