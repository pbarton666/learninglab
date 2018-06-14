#py_persistent.py
"""immortalize your stuff"""
import shelve

treasured_object={'team': 'Cubs', 
                  'place': 'Wrigley', 
                  'f_and_b': {'food': 'red hots', 'bev': 'Old Style'}
                  }
print("Original")
print("treasured object is {}".format(treasured_object))

shelve_file='persistent_shelve.shlv'

with shelve.open(shelve_file, writeback=True) as my_shelf:
          my_shelf['treasure']=treasured_object

with shelve.open(shelve_file, writeback=True) as my_shelf:
          print("Shelve here!")
          print("treasured object is {}".format(my_shelf['treasure']))
	
				
				

