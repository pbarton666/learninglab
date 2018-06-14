#py_log_2.py

import logging
LOG_FILENAME = "py_log_output.log"

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }
logging.basicConfig(filename=LOG_FILENAME, level=LEVELS['debug'])

def shout_out():
	logging.debug("shouting out at debug level")
	logging.info("shouting out at info level")
	logging.warning("shouting out at warning level")
	logging.error("shouting out at error level")
	logging.critical("shouting out at critical level")

shout_out()
logging.debug("*" * 30)

logging.getLogger().setLevel(logging.ERROR)

shout_out()
