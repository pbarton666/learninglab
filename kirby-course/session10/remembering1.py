# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23, 2016
Modified Mon Dec 12, 2016

@author: Kirby Urner

Remembering Python... 1

"""

# give me all the Python keywords please...
from keyword import kwlist as keywords
from random import choice  # randomness!

class GotOut(Exception): # customize your exceptions
    pass

class Die:
    
    def __init__(self):
        self.value = choice(range(1,7)) # won't be 7
    
    @property  # disguises a method call as an attribute
    def throw(self):
        self.value = choice(range(1,7))
        return self.value
        
    def __repr__(self):
        return str(self.value)

it = iter(keywords) # triggers __iter__ to add __next__

# simpler would be:
#for word in keywords:
#     print(word, end=" ")
    
for _ in range(len(keywords)): # more verbose than necessary
    print(next(it), end=" ")   # showing how next may be used
else:
    print()
    print("Those were keywords...")

die = Die()
while True:
    try:
        got = die.throw   # triggers __get__ method of throw
        print("Threw a {}".format(got))
        if got == 6:
            raise GotOut  # bail out of loop
    except GotOut:
        print("getting out...")
        break

abductees = []
    
def UFO(h):
    abductees.append(h)
    return h  # unharmed

@UFO
def f(x):
    return x + 2
    
@UFO    
def g(x):
    return x * 2

print("Abuctees (FunctionType elements: ", abductees)
print("calling f: ", abductees[0](100))
print("calling g: ", abductees[1](100))

# Composition of functions
print("f of g of 2 i.e. f(g(2)):", f(g(2)))
print("g of f of 2 i.e. g(f(2)):", g(f(2)))

# simple composer that eats functions, returns a function 

# compose = lambda m, n: lambda x: m(n(x))

def compose(m, n):
    def h(x):
        return m(n(x))
    return h

h = compose(f, g)
print("Lambda expression f(g(x)): ", h(2))

h = compose(g, f)
print("Lambda expression g(f(x)): ", h(2))


     