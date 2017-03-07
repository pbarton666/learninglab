
#py_animals.py

"""An introduction to the namedtuple object"""
from collections import namedtuple

#make a tuple with the tag 'Animal'
Animal=namedtuple('Animal', ('species', 'name'))

#specify this animal by providing the species and name
a1=Animal('gorilla', 'magilla')                 
print(a1)

#... and specify another
a2=Animal(species='gorilla', name='fred')
print(a2)

#we can call out the specifics using dot notation
print(a1.name, a2.name)

#... or, split the tuple containing the first animal
myspecies, myname = a1
print(myspecies)
print(myname)