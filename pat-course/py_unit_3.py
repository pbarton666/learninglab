#py_unit_4.py
import unittest
import tempfile
import os
import shutil

class RaiseTest(unittest.TestCase):
	
	def setUp(self):
		self.original_dir=os.getcwd()
		self.test_dir=tempfile.mkdtemp()
		os.chdir(self.test_dir)

	def test_tempfiles(self):
		"demonstrates creating temporary files"
		files_to_write=5
		for filenum in range(files_to_write):
			open("file"+str(filenum), 'w').close()
		myfiles=os.listdir()
		
		#do I have the right number of files
		self.assertEqual(len(myfiles), files_to_write)
		#check a name to be sure it's right
		lookfor="file0"
		self.assertTrue(lookfor in myfiles)
		
	def tearDown(self):
		os.chdir(self.original_dir)
		shutil.rmtree(self.test_dir)
			

if __name__=='__main__':
	unittest.main()