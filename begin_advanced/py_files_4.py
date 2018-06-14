#py_files_4.py
"""quite a crowed pickle barrel"""
import pickle
#make a couple objects
obj = [ [1, 2, 3],
        [4, 5, 5],
        [7, 8, 9]
      ]
obj1 = "howdy doody"
obj2 = set([33,43,53])


#open a binary file (remember, we're writing bytes)
pickle_file = "spicy"
with open(pickle_file, 'wb') as f:
	  pickle.dump(obj, f)
	  pickle.dump(obj1, f)
	  pickle.dump(obj2, f)

#let's kill the objects to prove this works
obj=None; obj1=None; ojb2=None   #possible, not recommended
	
with open(pickle_file, 'rb') as f:
	  recovered_obj=pickle.load(f)
	  recovered_obj1=pickle.load(f)
	  recovered_obj2=pickle.load(f)

#now, take a look
print("our objects survived!")
print(recovered_obj)
print(recovered_obj1)
print(recovered_obj2)
