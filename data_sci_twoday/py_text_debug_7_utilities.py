#py_text_debug_7_utilities.py
import logging
import pdb

def log_stack_info(s):
	"""logs quick list of the stack frames
	   and verbose version of each frame
	"""
	logger=logging.getLogger()
	for elem in s:
		logger.debug(elem)
		frame, filename, line_num, func, source_code, source_index = elem
		log_frame_locals(frame, filename, line_num)
		#kill frame to eliminate potential leaks cf. docs for details
		del frame
		
def log_frame_locals(frame, filename, line_num):
	"verbose logging of local variables in a stack frame"
	logger=logging.getLogger()
	fmt="{:<30}  {:<30}"
	logger.debug("")
	#we'll skip printing out redundant/uninteresting stuff
	excludes=('s', 'elem', '__warningregistry__')
	
	logger.debug("")
	msg='*'*20, filename, " at line ", line_num, ' ', '*'*20
	logger.debug(msg)
	logger.debug(fmt.format("name", "description"))
	logger.debug(fmt.format("-"*30, "-"*30))

	locals_dict=frame.f_locals  #could be f_globals, f_code
	for k, v in locals_dict.items():
		if not k in excludes:
			logger.debug(fmt.format(str(k), str(v)))	
	del frame 	
	pdb.set_trace()
