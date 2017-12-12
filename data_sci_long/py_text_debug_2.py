#py_text_debug_2.py

def buggy_code():
	x=1
	for i in range(-1, 1):
		print("i is now:  {}".format(i))
		print(1/i)		
		
buggy_code()		