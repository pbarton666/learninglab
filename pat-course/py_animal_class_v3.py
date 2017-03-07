# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:57:02 2016

#py_animal_class_v2.py


"""
from random import choice

class Animal:
    
    tricks = ["jumping", "playing dead", 
              "rolling over", "walking backwards"]
    
    def __init__(self, name, species, age, fav_food):
        self.name = name
        self.species = species
        self.__dict__["age"] = age # alternative to self.age = age
        self.fav_food = fav_food
        self.stomach = [ ]

    def __str__(self):
        return "Hi!  My name is {}".format(self.name)
        
    def __repr__(self):
        return "Animal(name={}, species={})".format(self.name, self.species)
        
some_animal = Animal("JoJo", "Monkey", 3, "banana")
some_animal.eat("banana")
print(repr(some_animal))  # force __repr__
print(some_animal)        # print calls __str__ if it finds one
some_animal.do_trick()
some_animal.eat("potato")
some_animal.do_trick()
some_animal.do_trick()
some_animal.eat("fritos")
some_animal.do_trick()
