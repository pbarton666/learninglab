#py_array.py

"how to use Arrays"
from array import array

#create an array
arr=array('i', [11, 12, 13] )
print("building an array")
print(arr)

#insert an element
to_insert=666
insert_pos=3
arr.insert(insert_pos, to_insert)
print("\ninserted {} at position {}".format(to_insert, insert_pos))
print(arr)

to_nuke=to_insert
arr.remove(to_nuke)
print("\ngot rid of {}".format(to_insert, insert_pos))
print(arr)


	



