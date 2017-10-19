#py_pickle.py
"""pickle your stuff for a long winter's nap"""
import pickle

treasured_object={'team': 'Cubs', 'place': 'Wrigley'}
pickle_file='persistent_pickle.pkl'

print("treasured object is {}".format(treasured_object))

with open(pickle_file, 'wb') as f:
		  pickle.dump(treasured_object, f)

with open(pickle_file, 'rb') as f:
		  recovered_obj=pickle.load(f)

print("recovered object is {}".format(recovered_obj))		  
assert treasured_object==recovered_obj
				

