
#py_regex_3.py
import re

regex = ( "cu" ,                #'cu'
          "0{\d4}",             #4 digits
          "x{1,3}" ,            #1,2, or 3 'x'
          "0{2,}",              #2 or more zeros
          "\W+",                 #contains at least one non alphanumeric characters
          )

target= ('Chicago Cubs', '1000000 dollars', "xxxooo", "$2500K")

for r in regex:
	for t in target:		
		result=re.search(r, t)
		if result:
			print("{:10} matched with {:10}".format(t, r))
		result=None
