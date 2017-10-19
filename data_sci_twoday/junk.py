"docstring for junk.py"
import string
import string
import string
import string
import string
import string
import string

def f_name():
    "docstring for f_name"
    print('f_name here')

def g():
    "some doc string"
    
def h(p1, p2):
    print(p1, p2)
    
def k(*aardvark):    
    print(aardvark)
    
def m(p1, p2, *args): 
    print(p1, p2)
    print(args) 
    
MON_IN_YR=12    
    
def p(p1=None, p2="pee, too"): 
    global globvar
    globvar=9
    print(globvar)
    if p1:
        print(p1)
    print(p2)
       
    
def n(**kwargs):
    print(kwargs)
    x=1
    
def v(p1, p2, *args, **kwargs):
    return (args, kwargs)

def mainxxxx():
    pass

a=1
#print('hi from junk.py again!!!!!!')    
    
if __name__=='__main__':
    import unittest
    mytests=unittest.TestCase()
    