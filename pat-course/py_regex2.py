
#py_regex_2.py
import re

regex = ( "[0123456789]" ,      #all digits
          "[0-9]",              #shorthand for all digits
          "[abc]" ,             #any of a, b, or c
          "[abc] [abc] [abc]",  #3 consecutive letters, each of which is a, b or c
          "[^0-9]",             #NOT a digit (the ^ in the first position negates  
          "x{1,5}",
          )

target= ('Texas', '123', "a", "abc")

for r in regex:
	for t in target:		
		result=re.search(r, t)
		if result:
			print("{:10} matched with {:10}".format(t, r))
		result=None
