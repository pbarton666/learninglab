import pkg1                    #./pkg1
from pkg1 import pgi1_object   #./pkg1/pgi1_object.py
from pkg1 import pgi1_string   #./pkg1/pgi1_string.py
from pkg2 import pgi1_object   #./pgk2/pgi1_object.py
from pkg2 import pgi1_string   #./pgk2/pgi1_object.py

from pkg2 import pgi1_object as p2_object
from pkg2 import pgi1_string as p2_string

#py_test_debug_5.py
import inspect

class MyClass:
	def __init__(self, arg):
		self.instance_var=a(arg)

def a(x): 
	#create a tuple of stack elements
	s=inspect.stack()
	#print summary information
	for elem in s:
		print(elem)
	
	#print nicely-formatted, detained information
	fmt="{:<30}  {:<30}"
	print()
	#we'll skip printing out redundant/uninteresting stuff
	excludes=('s', 'elem', '__warningregistry__')
	for frame, filename, line_num, func, source_code, source_index in s:
		print()
		print('*'*20, filename, " at line ", line_num, ' ', '*'*20)
		print(fmt.format("name", "description"))
		print(fmt.format("-"*30, "-"*30))
		
		locals_dict=frame.f_locals  #could be f_globals, f_code
		for k, v in locals_dict.items():
			if not k in excludes:
				print(fmt.format(str(k), str(v)))
		#kill frame to eliminate potential leaks cf, docs for details
		del frame  

if __name__=='__main__':
	instance=MyClass(666)
