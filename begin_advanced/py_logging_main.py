
#py_logging_main.py

import logging
LOG_FILENAME = "py_log_output.log"
LOG_FORMAT = "%(asctime)s  called from  %(filename)s: %(message)s"

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format=LOG_FORMAT)
logging.getLogger("logger")
logging.debug('started logging')
