#py_text_debug_6.py

import inspect
import py_text_debug_5 as module
#import inspect as module

fmt="name: {:<15} type: {:<15} args: {:<15} *args: {:<10} **kwargs:{:<10}"
for name in dir(module):
	obj=getattr(module, name)
	try:
		specs=inspect.getargspec(obj)
	except:
		pass 
	args, varargs, keywords, defaults=specs
	print (fmt.format (name, str(type(obj)), str(args), 
	                   str(varargs), str(keywords)))

listing, _ = inspect.findsource(module)
print()
for line_no, code in enumerate(listing, 1):
	print(line_no, code)
	if line_no >8: break

