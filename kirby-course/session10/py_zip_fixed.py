#py_zip.py

"""This routine will let you zip up your course work.
   The function extract() will upzip it for you when
   you get back to your home base"""

import zipfile
import os
import sys

ARCHIVE_NAME="course_materials.zip.masked"

#id which directory to zip up and grab its contents
this_dir=os.getcwd()

#this creates a generator object of all your fs components
file_sys_contents=os.walk(this_dir)

#create the zip file object
try:
	archive=zipfile.ZipFile(ARCHIVE_NAME, mode='w')
except:
	print("Sorry, couldn't create a zip file")
	sys.exit()

#if we're able to create the file, ransack the walk generator
try:
	
		for root, folders, files in file_sys_contents:
			# write all the folders
			for folder_name in folders:
				absolute_path = os.path.join(root, folder_name)
				relative_path = absolute_path.replace(this_dir + '\\', '')
				print("Adding {} to archive.".format(absolute_path))
				archive.write(absolute_path, relative_path)
			
			#write all the files	
			for file_name in files:
				absolute_path = os.path.join(root, file_name)
				relative_path = absolute_path.replace(this_dir + '\\', "")
				#don't zip archives (prevent recursion) or .pyc files
				###following line is fixed
				if not zipfile.is_zipfile(absolute_path) and not absolute_path.endswith("zip") and \
				   not file_name.endswith('masked') and \
				   not absolute_path.endswith("pyc"):		                     
					print ("Adding {} to archive.".format(absolute_path))
					archive.write(absolute_path, relative_path)
				
		print ("{} created successfully.".format(ARCHIVE_NAME))
		
except IOError as message:
	print (message)
	sys.exit(1)
except OSError as message:
	print (message)
	sys.exit(1)
except zipfile.BadZipfile as message:
	print (message)
	sys.exit(1)
finally:
	archive.close()
	
	
def extract():
	"extracts the archive"
	extract_dir="course_work"
	try:
		os.mkdir(extract_dir)
	except:
		print("couldn't create directory {}.".format(extract_dir))
	with zipfile.ZipFile(ARCHIVE_NAME) as zf:
		zf.extractall(path=extract_dir)
	
	
	
	
	
	
