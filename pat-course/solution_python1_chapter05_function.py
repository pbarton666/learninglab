#solution_python1_chapter05_function.py

def outer_function(operation, subtract_this):
	"takes an operation and a number to subtract"
	thing_to_subtract=subtract_this
	def add_me(a, b):
		"adds two numbers"
		return (a + b) 
	
	def mult_me(a, b):
		"multiplies two numbers"
		return a * b 
	
	#a dict of possibilities
	op_dict={"addition": add_me,
	         "multiplication": mult_me}
	

	def inner_function(a,b):
		"inner-most function"
		func=op_dict.get(operation, None)
		nonlocal thing_to_subtract
		fs= "You asked me to perform {} on {} and {} then subtract {}.  I got {}."
		if func:
			print(fs.format(operation, a, b, subtract_this, func(a,b)-subtract_this))
		else:
			print("The operation you provided {} is not yet supported")

	return inner_function	


execute_this_with_two_args=outer_function("addition", 10)
execute_this_with_two_args(2,3)



