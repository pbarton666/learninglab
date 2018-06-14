#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#py_format.py
"""
Side nte:   The statements at the top are purely optional, but you'll run into
syntax like this occasionally.  The first is an example of a "hash-bang" tag
and directs the script to use the Python executable found in this location.  
It only works in Linux systems, and only if the executable is available

The second directs Python to use UTF-8 encoding if it's available.
"""

#Basic usage
stg = "{} {}".format("Hey","Joe")
print(stg)

#numbered fields ('all or none' here)
stg = "{0} {1} {2}".format("George", "Paul", "John")
print(stg)

stg = "{2} {1} {0}".format("George", "Paul", "John")
print(stg)
print()

stg = """\
Dear {donor},
  I'm running for {office} and would like to shake
  you down for a ${dollars} contribution.
             
  Sincerly,
     - {candidate}"""

#named fields ('all or none'; note no quotes around names)
print(stg.format(donor = "SuperPAC", office = "President", 
                 dollars =100, candidate = 'Pat'))
print()

#10 wide, accept default justification
stg = "{0:<10} {1:<10}  {1:<10}"
print(stg.format("Presenting: Addition!!!", ''))
print(stg.format("output", "input"))
print(stg.format("=" * 6, "=" * 6))
print(stg.format(4, 2, 2))
print(stg.format(8, 4, 4))

print()	

#example of numeric base "casting"; 
# {0:>#16b}  means “the first argument, right justified 
#   in a 16-character wide field; the combination of
#   the # before “16” and b afterward requests 
#   binary output

stg = "{0:>6} = {0:#16b} = {0:#06x}"  #note the  '#..b'  and '#0..x' 
for i in (1, 23, 456, 7890):
	print(stg.format(i))
