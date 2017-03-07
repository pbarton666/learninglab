#py_log_3.py

import logging
WOMBAT=logging.WARNING + 1

LOG_FILENAME = "py_log_output.log"
LOG_FORMAT = "%(asctime)s  called from  %(module)s:  %(lineno)d    %(message)s"

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format=LOG_FORMAT)

class WombatException(Exception):
    logger=logging.getLogger()
    logger.log(WOMBAT, "Wombat!")
    
def do_raise_wombat():        
    raise WombatException

do_raise_wombat()
