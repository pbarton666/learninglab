# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4, 2016
Modified Mon Dec 12, 2016

@author: Kirby Urner

Show how entering a context triggers the __enter__
tripwire.  On __exit__ you may set off the emergency
buzzer (return False), or not (return True)
"""

class CodeCastle:
    
    def __init__(self):
        self.me = "I will be your guide"
        
    def __enter__(self):
        print("You have entered the castle")
        return self
        
    def __exit__(self, *oops):  # 3-tuple
        if oops[1]:
            print("Arg 0:", oops[0])
            print("Arg 1;", oops[1])
            return False
        return True # all is well

try:
    with CodeCastle() as guide:
        print("We're in!")
        print(guide.me)
        raise ValueError("Uh oh!")
    print("You have left the castle normally.")
except:
    print("Something bad happened")
    
print("We're done")
    
# End of Story
    