import logging
LOG_FILENAME = "py_log_output.log"

LOG_FORMAT = "%(asctime)s %(name)s:%(levelname)s:%(filename)s function:%(funcName)s line:%(lineno)d %(message)s"

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

logging.basicConfig(filename=LOG_FILENAME, level=LEVELS['debug'], format=LOG_FORMAT)

logging.getLogger("logger")
logging.debug('started logging in main')

if __name__=='__main__':
    #logger
    pass   