#py_files_3.py
"""quite a pickle"""
import pickle
#make an object
obj = [ [1, 2, 3],
        [4, 5, 5],
        [7, 8, 9]
      ]

print("hey, we've got an object")
print(obj)

#open a binary file (remember, we're writing bytes)
pickle_file="brine"
with open(pickle_file, 'wb') as f:
	pickle.dump(obj, f)

#let's kill the object to prove this works
obj=None
if not obj:
	print("\nno object here!")
	
with open(pickle_file, 'rb') as f:
	recovered_obj=pickle.load(f)

#now, take a look
print("\nPresto, chango, here's our recovered object!")
print(recovered_obj)
