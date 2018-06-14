#py_unit_2.py
import unittest

class FirstTest(unittest.TestCase):
	def setUp(self):
		"setUp() runs before every test"
		self.msg="Sorry, Charlie, but {} is not the same as {}."
	def tearDown(self):
		"tearDown runs after every test"
		pass
	def test_me(self):
		"this test should pass"
		first=1
		second=2
		self.assertEqual(first,1, msg=self.msg.format(first, second))
	def test_failing(self):
		"this test should fail"
		first=1
		second=2
		self.assertEqual(second,1, msg=self.msg.format(first, second))
	def test_passing(self):
		"this test should pass, too"
		self.assertEqual("b", "b")
	def test_passing_a_failing_test(self):
		"this test should pass, even though it 'fails'"
		self.assertNotEqual("a", "b")		
		
	
if __name__=='__main__':
	unittest.main()