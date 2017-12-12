#py_text_debug_3.py

DEBUG_MODE = True

def buggy_code():
	for i in range(-1, 1):
		print("i is now:  {}".format(i))
		if DEBUG_MODE and i==0: import pdb; pdb.set_trace()
		print(1/i)		

buggy_code()		