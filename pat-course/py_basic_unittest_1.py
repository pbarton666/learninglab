#py_basic_unittest_1.py

def odd_man_out(inp):
	"""If input looks like an odd integer, return
	    twice its value; otherwise, return None"""
	try: #Is it a number at all?  If not, give up.
		inp/1
	except:
		return None
	try: #If it's a number, can it be cast as an integer?
		inp=int(inp)
	except:
		return None
	#If it's a number, is it odd?
	if inp % 2:  #returns 0 if even
		return(inp*2)

if __name__=='__main__':
	import unittest
	class tester(unittest.TestCase):
		def test_odd_integer(self):
			self.assertEqual(odd_man_out(3), 6)
		def test_even_integer(self):
			self.assertEqual(odd_man_out(4), None)
	unittest.main()