#py_persistent_2.py
"""pickle your stuff for a long winter's nap"""
import pickle
from py_persistent_3 import THIS_YEAR

print("imported THIS_YEAR, which is {}".format(THIS_YEAR))

pickle_file='this_year.pkl'
with open(pickle_file, 'wb') as f:
		  pickle.dump(THIS_YEAR, f)


