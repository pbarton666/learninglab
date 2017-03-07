# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23, 2016
Modified Mon Dec 12, 2016

@author: Kirby Urner

Remembering Python... 2

"""

# I, Python am built from types, such as builtin types:

the_builtins = dir(__builtins__) # always here

for the_string in ["list", "tuple", "property", 
                   "dict", "int", "float", "next", "namedtuple"]:
    if the_string in the_builtins:
        print("Yes I am a native type: ", the_string)
        try:
            assert type(eval(the_string)) == type # all types in this club
        except AssertionError:
            print("in __builtins__ but not a type: ", the_string)
    else:
        print("No, I'm not in __builtins__: ", the_string)

# usually up top
from string import ascii_lowercase as all_lowers
from random import shuffle

class P:
    """
    class Px is the more sophisticated version of this class
    """
    def __init__(self, p=None):
        if not p:
            original = all_lowers + ' '
            scrambled = list(original)
            shuffle(scrambled)            
            self.perm = dict(zip(original, scrambled))
        else:
            self.perm = p
        
    def __invert__(self):
        """reverse my perm, make a new me"""
        reverse = dict(zip(self.perm.values(), self.perm.keys()))
        return P(reverse)  # <-- new P instance
        
    def encrypt(self, s):
        output = ""
        for c in s:
            output += self.perm[c]
        return output
            
    def decrypt(self, s):
        rev = ~self  # <-- new P instance
        return rev.encrypt(s) # <-- symmetric key
        
if __name__ == "__main__": # only run if this module is top level
    p = P()
    m = "able was i ere i saw elba"
    c = p.encrypt(m)
    print(m)  # plaintext
    print(c)  # ciphertext
    d = p.decrypt(c)
    print(d)
