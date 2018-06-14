#py_unit_1.py
import unittest

class FirstTest(unittest.TestCase):
	def test_me(self):
		first=1
		second=2
		msg="Sorry, Charlie, but {} is not the same as {}."
		self.assertEqual(first,1, msg=msg.format(first, second))
		
if __name__=='__main__':
	unittest.main()