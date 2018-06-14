#py_files_2.py

import os
import tempfile

#get the name of the current directory
original_dir=os.getcwd()
print('we started in')
print(original_dir)

#go to the parent directory
os.chdir('..')
print("\nnow we're in")
print(os.getcwd())

#get the original directory contents
dir_contents = os.listdir(original_dir)

#classify the first few objects
print("\nexamining the contents of {}".format(original_dir))
for _ in range(5):
	fs_object_name = dir_contents.pop()
	fs_object = os.path.join(original_dir, fs_object_name)
	label = ''
	if os.path.isdir(fs_object): 
		label = 'dir'
	if os.path.isfile(fs_object): 
		label = 'file'
	if os.path.islink(fs_object): 
		label = 'link'
	print(label, fs_object_name)
	
#checking for a directory, creating it if it's not there
look_for='junk'
look_in=original_dir
print("\nIf you don't have a junk directory, let's make one\n")
if not os.path.exists(os.path.join(look_in, look_for)):
	os.mkdir(os.path.join(look_in, look_for))
	
#another way, using exceptions
try:
	os.mkdir(os.path.join(look_in, look_for))
except:
	pass

#print out the methods in the os module
print("\nGee, lookee at all the stuff we can do with os!\n")
for obj in dir(os):
	first_char = obj[0]
	#filter out the internal methods and CONSTANTS
	if not first_char == "_" and not first_char.isupper():
		print(obj)
	

