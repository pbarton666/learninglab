
#py_regex_4.py
import re

regex =  "Cubs" 
target= 'Chicago Cubs'

compiled=re.compile(regex)

result=compiled.search(target)	
if result:
	print("{:10} matched with {:10}".format(target, regex))
	print("span", result.span())
	print("start", result.start())
	print("end", result.end())
	
