#py_basic_unittest.py

import unittest

plant_dict={'raspberry': 'rubus',
            'elm'      : 'ulmus',
            'maple'    : 'acer'
            }
look_for='alder'
default='SOMETHING.  I dunno'

class tester(unittest.TestCase):
	def test_found_OK(self):
		self.assertEqual(plant_dict.get('elm'),'ulmus')
	def test_not_found_None(self):
		self.assertEqual(plant_dict.get('sumak', None), None)
	def test_not_found_string(self):
		self.assertEqual(plant_dict.get('ash', 'no_ash'), 'no_ash')
		
unittest.main()