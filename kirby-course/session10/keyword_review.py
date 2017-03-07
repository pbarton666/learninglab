# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18, 2016
Modified on Mon Dec 12, 2016

@author: Kirby Urner

=== Keywords

Python's keywords, categorized as:

Boolean -- logical tests and results
Scope -- pertaining to namespace
Definition -- creating and destroying objects
Flow -- what happens next, looping, passing control

Then convert the resulting dict out to json as a
text file and read it back in for display -- note
the nice indentation, applied by json.dump().

import as keywords only, or run as '__main__' 
for file-based test
"""
import json

keywords = \
{
"Boolean": [
'False',  # same as 0
 'None',
 'True',  # alias for 1
 'and',
 'in',    # triggers __contains__
 'is',    # as distinct from ==
 'not',
 'or' 
],
"Scope": [
 'as',    # used with context manager and import
 'from',
 'global',
 'import',
 'nonlocal',
 'with'   # works with __enter__, __exit__ protocol
 ],
"Definition": [
 'class',
 'def',   # for function generators and coroutines too
 'del',
 'lambda' # makes a callable object of one expression
 ],
"Flow" : [
 'assert',    # raises exception if untrue
 'break',     # escape the loop
 'continue',  # short circuit
 'elif',
 'else',
 'try',       # get ready for exceptions
 'raise',     # part of many a civilized API
 'except',    # for handling exceptions
 'finally',   # when leaving a try block, always
 'while',
 'for',
 'if',
 'pass',      # dummy statement
 'return',    # surrender control with object
 'yield',     # pause / continue, able to accept
 'async',     # enables awaits
 'awaits']    # alternative to yield from
}

if __name__ == "__main__":
    with open('outfile.json', 'w') as f:
        json.dump(keywords, f, indent=8)
    
    with open('outfile.json', 'r') as f:
        show_me = f.read()
    
    print(show_me)
    
    # convert from a string back into a dict:
    the_dict = json.loads(show_me)
    print("Keywords relating to Scope flavor\n", 
          the_dict["Scope"])  # does this work?
