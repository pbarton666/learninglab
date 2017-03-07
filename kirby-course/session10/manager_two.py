# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:20:01 2016

@author: Kirby Urner

Here we're using the generator function based 
approach to definition a context manager.  Just
decorate with @contextmanager

On except you may propagate the exception
with raise, or return None to say it's handled.
"""

import contextlib

@contextlib.contextmanager
def CodeCastle():
    try:
        me = "I will be your guide"
        print("You have entered the castle")
        yield me
    except Exception as the_problem:
        print(type(the_problem))
        print(the_problem)
        # raise # comment out if exception handled
    finally:
        print("Exiting context")

try:   
    with CodeCastle() as guide:
        print(guide)
        print("We're in!")
        # raise ValueError("Uh oh!")
    print("You have left the castle normally.")
except:
    print("Something bad happened")

print("We're done!")    
# End of Story
    