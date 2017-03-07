#py_time_2.py
from datetime import datetime, timezone

now_here = datetime.now()
print("Now, this timezone            : ", now_here)
now_uk = datetime.now(timezone.utc)
print("Now, in England               : ", now_uk)
the_date = now_uk
print("Days since 01-01-0001         : ", the_date.toordinal())
epoch = datetime(1970,1,1, tzinfo=timezone.utc)
print("01/01/1970 timestamp          : ", epoch.timestamp())
print("Now in English timestamp      : ", now_uk.timestamp())
delta = now_uk - epoch
print("Time delta in seconds         : ", delta.total_seconds())


