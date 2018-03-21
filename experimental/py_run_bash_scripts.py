"""Script to test execution of bash scripts, gathering
      the results, combining them and saving them.

	  @author 'Pat Barton'	  
"""



"""This demo is simple, but shows all the key steps required to integrate
     existing bash scripts with you python codes.

   Exactly what the bash scripts do is not important so we'll 
      spin up some trivial ones.  We'll just make some up.  For
	  demo purposes all will do the same thing - return the names
	  of files (ls/dir command) - from their directories.
	  
   We'll create different directories for each of three bash scripts
      and populate the directories with files named so we know where
	  they camre from.
	  
	All this happens in setup_scratch_dirs() - not that all this functionality
	  is isolated from the rest of the code.  That way it'll be easy to substitute
	  "real" bash scripts from your own directories.   Note the use of 
	  tempfile.mkdtemp() - this writes a scratch directory somewhere safe.   Note
	  also that we're exercising good manners by cleaning up the mess using
	  shutil.rmtree.
	  
	=======
	The bash files will go out into the world and do something.  All this functionality
	  is handled in run_scripts().  Note, again, the isolated functionality - this makes things
	  easy to maintain.   We run the scripts and capture their output with the 
	  subprocess.check_output() method.
	  
	===
	At the end of the day we want to do something with the output.  That's all handled in
	  the process_output() function.   Naturally, you'll want to "roll your own" here, but you 
	  know where to put it.
	  
	===
	The global namespace of the module is uncluttered.   The bit at the top wrangles the 
	  imports and makes sure we remember the original directory.   The bit at the bottom
	  cleans things up and ensures that we leave the working directory right where we found it.
"""

import tempfile
import os
import shutil
import subprocess

NUM_SCRIPTS = 3

#make a temp dir and switch into it.
orig_dir = os.getcwd()        #remember original dir
temp_dir = tempfile.mkdtemp() #returns name of new dir
os.chdir(temp_dir)            #switch to temp dir

def setup_scratch_dirs():
	"""This routine makes subdirectories in scratch folder.  Each
	   gets populated with a few empty files and its own bash script.
	   So it'll look like:
	   scratch\
	      subdir0\
		     subdir0_file0
			 subdir0_file1
			 subdir0_file2
			 script0.sh
		The script file just contains the command 'ls' and will list the
		files in its subdir (makes output easy to check)
		
		A list of the script files is returned.
	"""		 
	scrip_paths=[]
	for s in range(NUM_SCRIPTS):
		subname = "subdir" + str(s)
		sub = os.mkdir(subname)  #make sudirs named 'subdir0', etc.
		os.chdir(subname)                      #switch to subdir
		for f in range(5):   
			filename = "subdir" + str(s) + "_file" + str(f)
			open(filename, 'w').close()
		
		#create a script file and a file handler
		scriptname = 'script' + str(s) + ".sh"
		scrip_paths.append(os.path.join(os.getcwd(), scriptname))
		with open(scriptname, 'w') as script:
			script.write("#! /bin/bash\n")
			script.write("ls\n")     #lists contents of the director
			
		os.chmod(scriptname, 0o777)   #let anyone do anything with the script
		
		os.chdir('..') #switch to scratch dir
	
	return scrip_paths

def run_scripts(scripts):
	"""Expects an iterable object (list, tuple, etc.) containing
	   fully-specified path to script file.  Runs each script, 
	   captures the output, and does something with the output.
	   
	   The subprocess module has tons of options.  You can read
	   all about them here:
	   
	   https://docs.python.org/3/library/subprocess.html
	   
	   Output is stored in a list, one element for each script,
	   and returned.
	   
	"""
	output_list=[]
	for index, s in enumerate(scripts):
		#split path name from script name
		sdir, sname = os.path.split(s)  
		#run the script using its dir as the cwd, capture output
		os.chdir(sdir)
		output = subprocess.check_output(s)
		output_list.append(output)
	return output_list
	


def process_output(output):
	"""Does something with the output, which enters this function
	   as a list.  Do anything you want here, I'm just having fun"""
	
	for i in range(len(output)):
		"this makes a list from the return of a ls from linux"
		output[i] = output[i].split()
	
	stg = "{} HealthCheckPassed \n\t{} INROTATION \n\t{} STATUSCODE"	
	for result0, result1, result2 in zip(output[0], output[1], output[1]):
		print(stg.format(result0, result1, result2))
		

scripts = setup_scratch_dirs()	
output = run_scripts(scripts)
process_output(output)

os.chdir(orig_dir)
shutil.rmtree(temp_dir)	

		
	  