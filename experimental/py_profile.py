#py_profile.py
import cProfile

thing_to_test=\
"""
for i in range(100000):
    x=i^5
"""
        
cProfile.run(thing_to_test)    


