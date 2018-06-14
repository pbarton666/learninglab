
#py_regex_1.py
import re

regex = 'x'  #what we're looking for
target = 'Texas'
result = re.search(regex, target)

if result:
	print("Yay!  {} found.".format(regex))
	print("The found object is: {}".format(result))