#py_array_1.py

"more on arrays"
from array import array

#create a new array
rows=3; cols=3; index=0   #poor practice, by the way
print("\nadding elements to a new array")
new_arr=array('i')
for row in range(rows):
	for col in range(cols):
		new_arr.insert(index,row*10+col)
		index+=1
print(new_arr)
print("the first row is: {}".format(new_arr[0:cols]))
print("the second row is: {}".format(new_arr[cols:2*cols]))
print("the sum of elements is {}".format(sum(new_arr)))


	



