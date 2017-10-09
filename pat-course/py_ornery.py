# -*- coding: utf-8 -*-
# py_ornery.py
"""
This type of object gets along with nobody!

or·ner·y
ˈôrn(ə)rē/
adjective North American informal
adjective: ornery

    bad-tempered and combative.
    "some hogs are just mean and ornery"
    synonyms:	grouchy, grumpy, cranky, crotchety, cantankerous, 
    bad-tempered, ill-tempered, dyspeptic, irascible, waspish
    
自 = self in Chinese, disregard errors

Using this character in place of self to prove self is 
not a keyword, just a placeholder.  Any legal name will
work, just "self" is universally accepted by convention.

Make sure you keep the utf-8 directive at the top, 
especially on Windows.
"""

class Ornery:
  
  def __init__(自, name="Fred"):
    自.name = name
    print("A sourpuss is born!")
    
  def __getitem__(自, key):
    return "How dare you touch me with those brackets!"
    
  def __call__(自, *args, **kwargs):
    return "Don't call me at home!"
    
  def __getattr__(自, attr):
    return "I'm insulted you'd suppose I'd have '{}'".format(attr)
    
  def __repr__(自):
    return "Don't bother me!  Go away."
  
  def __invert__(自):
    return "I can't invert, are you kidding?"

def main():
    obj = Ornery()        # __init__
    print(obj)            # __repr__
    print(obj.mood)       # __getattr__
    print(obj("Hello?"))  # __call__
    print(~obj)           # __invert__
    
if __name__ == "__main__":
    main()