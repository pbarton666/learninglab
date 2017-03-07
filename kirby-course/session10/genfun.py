# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:49:25 2017

Lets learn about itertools!
https://docs.python.org/3.6/library/itertools.html
STEM%20Mathematics.ipynb

@author: Kirby Urner
"""

from itertools import islice, permutations, combinations, chain

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)
    
def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)
    
def fibo(a=0, b=1):
    """
    http://oeis.org/A000045
    """
    while True:
        yield a
        b, a = a + b, b
     
gen = fibo()     
print([next(gen) for _ in range(30)]) 

gen = fibo()
print(list(islice(gen, 0, 30)))  

gen = fibo()
print("200th Fibonacci:", nth(gen, 200))

print() 
print("Permutations")
allperms = permutations(("heart", "diamond", "club", "spade"))
for perm in allperms:
    print(perm)
print()

print("Combinations")    
allcombs = combinations(("heart", "diamond", "club", "spade"), 2)
for perm in allcombs:
    print(perm)
    
nested = ["I", ["am", "a", "nested"], ["list of", "lists"]]

print("Flattened")
for n in flatten(nested):
    print(n)
    
def pascal():
    row = [1]
    while True:
        yield row
        row = [i+j for i,j in zip([0]+row, row+[0])]

# play
print(":".join(map(lambda n: "{:>3}".format(n), [1, 2, 3, 4])))

print("{0:=^60}".format(" Pascal's Triangle "))
print()
for r in islice(pascal(),0,11):
    print("{:^60}".format("".join(map(lambda n: "{:>5}".format(n), r))))
    