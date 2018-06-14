#py_function_7_upgraded.py

"""With function dispatch logic, we can add capability with minimal
     disruption to existing code, fewer chances of making mistakes, 
     and with no worries about the logical sequence of elif statements.
     Changes are flagged below"""

from random import choice
 
def f_upper():
   return str.upper
def f_lower():
   return str.lower
def f_swap():
   return str.swapcase

##*** add the new function to be dispatched
def f_title():
   return(str.title)

function_mapper={'up': f_upper, 'lower': f_lower, 'swap': f_swap}

##*** add the new function to the mapper dict
function_mapper['title'] = f_title

choices = ['up', 'lower', 'swap']
##*** add a new choice
choices.append('title')

my_string='Lions and Tigers and Bears, Oh MY!'

for i in range(3):
   mychoice=choice(choices )
   print(function_mapper[mychoice]()(my_string))
     
    