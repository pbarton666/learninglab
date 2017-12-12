#py_text_debug_7_main.py
import logging
import inspect

from py_text_debug_7_utilities import log_frame_locals, log_stack_info

logging.basicConfig(filename= "py_log_output.log")
logger=logging.getLogger()
logger.level=logging.DEBUG

class MyClass:
	def __init__(self, arg):
		self.instance_var=a(arg)

def a(x): 
	#create a tuple of stack elements
	s=inspect.stack()
	if logger.level==logging.DEBUG:
		log_stack_info(s)

if __name__=='__main__':
	instance=MyClass(666)