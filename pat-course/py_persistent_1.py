#py_persistent_1.py
"""pickle your stuff for a long winter's nap"""
import pickle

treasured_object={'team': 'Cubs', 
                  'place': 'Wrigley', 
                  'f_and_b': {'food': 'red hots', 'bev': 'Old Style'}
                  }

pickle_file='persistent_pickle.pkl'

print("Original")
print("treasured object is {}".format(treasured_object))

with open(pickle_file, 'wb') as f:
		  pickle.dump(treasured_object, f)

with open(pickle_file, 'rb') as f:
		  recovered_obj=pickle.load(f)
		  
test=treasured_object==recovered_obj
if not test:
		  print('whoops, pickle failed for {}'.format(treasured_object))
else:
		  print("pickle here!")
		  print("recovered object is {}".format(recovered_obj))

				
				

