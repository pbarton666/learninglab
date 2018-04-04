#py_profile.py

"Basic usage of cProfile/profile"

try:	
	import cProfile as profiler
except:
	
	import profile as profiler

thing_to_test=\
"""
for i in range(100000):
    x=i^5
"""
        
profiler.run(thing_to_test)    


