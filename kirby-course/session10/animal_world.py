# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12, 2016

@author: Kirby Urner

Defines animals but does not create any.
See animal_world_test.py for example tests

"""

class Animal:
    
    def __init__(self, nm):
        self.name = nm
        self.stomach = []
        self.eyes = 2

    @property
    def name(self):
        return self.__name # buried secret
        
    @name.setter  # name is now a property type object
    def name(self, new_name):
        if new_name in self.no_like:
            raise ValueError("Me no like that name")
        self.__name = new_name
        
    @name.deleter
    def name(self):
        print("resetting to None")
        self.__name = None
        
class Dog(Animal):  # inheritance
    
    no_like = ['Kitty', 'Wall-e', 'Duck']

class Cat(Animal):
    
    no_like = ['Doggy', 'Rover', 'Duck']


class Duck(Animal): 
    
    no_like = ['Doggy', 'Kitty', 'Wall-e']

