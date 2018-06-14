#py_time_3.py
from datetime import datetime
date_format = "%d, %b %Y"   
now = datetime.now()

print("Hello! Today is {}.".format(now.strftime(date_format)))



