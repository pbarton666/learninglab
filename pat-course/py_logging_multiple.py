
#py_logging_multiple.py
#   adapted from docs/python.org/howto/logging-cookbook.html Recommended!

import logging

LOG_FILENAME = "py_log_output.log"

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=LOG_FILENAME)

# define a new Handler object to write certain messages to sys.stderr
#creates an instance of StreamHandler
console = logging.StreamHandler()
#... customizes it
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
#...and attaches it to the logger
logging.getLogger('').addHandler(console)

# Let's try it out.
logging.critical('Wombats have been detected!')
logging.warning('just more boring log content')

