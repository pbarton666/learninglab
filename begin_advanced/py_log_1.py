
#py_log_1.py

import logging
logging.basicConfig(filename="py_log_output.log", level=logging.DEBUG)

#this writes a line to the file
logging.debug("Yup, I'm debugging")


