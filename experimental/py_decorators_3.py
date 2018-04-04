#py_decorators_3.py

"Demonstrating @wraps to preserve original function's name"

from functools import wraps

def decorator(func):
	@wraps(func)
	def decorated_func( *args, **kwargs):		
		print ("Originating function:  {}".format(func.__name__))
		return func( *args, **kwargs)
	return decorated_func
	
@decorator
def ordinary_function(x):
	print("hi, there from {}!\n".format(ordinary_function.__name__))
	return x ** 3	

try:		
	print("{} -> {}".format(3, ordinary_function(3)))
except TypeError:
	print("ordinary_function exists in namespace, but is None type")
	print("is ordinary_function None?   {}".format(ordinary_function is None))
		
x = 1	