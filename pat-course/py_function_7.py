#py_function_7.py

from random import choice
 
def f_upper():
   return(str.upper)
def f_lower():
   return(str.lower)
def f_swap():
   return(str.swapcase)

function_mapper={'up': f_upper, 'lower': f_lower, 'swap': f_swap}

my_string='Lions and Tigers and Bears, Oh MY!'
for i in range(3):
   mychoice=choice( ['up', 'lower', 'swap'] )
   print(function_mapper[mychoice]()(my_string))
   

#breaking it down a bit:
#mychoice                                                #returns something like 'up'
#function_mapper['up']                                   #f_upper
#function_mapper[mychoice]()                             #str.upper function
#function_mapper[mychoice]()(my_string))                 #str.upper('Lions and Tigers and Bears, Oh MY')   
    