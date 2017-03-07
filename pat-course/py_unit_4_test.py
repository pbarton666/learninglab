#py_unit_4_test.py
import unittest
from py_unit_4_code import add_numbers

class AnotherTest(unittest.TestCase):

	def test_addition(self):
		"can we add?"
		self.assertEqual(add_numbers(2,2), 4)

if __name__=='__main__':
	unittest.main()