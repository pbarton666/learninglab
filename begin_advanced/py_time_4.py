#py_time_4.py
from datetime import datetime
now = datetime.now()
exact_format="%Y-%m-%d %H:%M"
print("Or, more precisely, {}.".format(now.strftime(exact_format)))



