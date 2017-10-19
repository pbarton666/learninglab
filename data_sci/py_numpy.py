#py_numpy.py

"""This script contains code to demonstrate basic operations
   using numpy arrays
"""   


#import the library:
import numpy as np

#create an array simply by populating it
a=np.zeros((3,4)); b=np.ones(3)
arr = np.array([1, 2, 3])  
print(arr)
print(type(arr))
print()

#the array knows a lot about itself and can be sliced like a list
print(arr.shape)
print(arr[-1])
print(arr[1:3])
print()

#you can create a 2d array like a list of lists
arr2d = np.array([[1,2,3],[4,5,6], [7, 8, 9]])  
print(arr2d)
print (arr2d.shape)
print(arr2d[2, 1])
print()

#now, you can address elements with 2d slicking
new2d=arr2d[1:, 1:]
print(new2d)
print()

#you can address one 'dimension' at a time
new1d_row=arr2d[1,]
print(new1d_row)
new1d_col=arr2d[:,1]
print(new1d_col)
print()

#scalar options are easy
double=arr2d*2
print(double)
square=arr2d**2
print(square)
print()

#you can make "deep copies" just like lists
copy_arr2d=arr2d[:]
copy_arr2d[1,]=copy_arr2d[1,]*2
print(copy_arr2d)
print()

#stats
print("max", arr2d.max())
print("mean", arr2d.mean())
print("min", arr2d.min())
print("sd", arr2d.std())
print("sum", arr2d.sum())
print("transpose\n", arr2d.T)
print()

#row, column masks for a diagional
row_mask=np.array([0,1,2])
col_mask=np.array([0,1,2])
diagonal=arr2d[row_mask, col_mask]
print(diagonal)

#or, just use the built-in
print(arr2d.diagonal())
print()

#it's possible to create a boolean mask
boolean_ix=arr2d % 2 == 0  #filter evens
print(boolean_ix)

evens=arr2d*boolean_ix
print(evens)
print()

#extract evens
just_evens=arr2d[boolean_ix]
print(just_evens)
print()


#matrix ops
a_arr = np.array([[1,2],[3,4]])
b_arr = np.array([[5,6],[7,8]])
c_arr = np.array([9,10])
d_arr = np.array([11, 12])

# Scalar Products
print("scalar product of:\n", c_arr, "\nand\n", d_arr, '\n')
print (c_arr.dot(d_arr))
print (np.dot(c_arr, d_arr))
print()

# Matrix Products 
print("matrix product of:\n", a_arr, "\nand\n", c_arr, '\n')
print (a_arr.dot(c_arr))
print (np.dot(a_arr, c_arr))
print()

print("matrix product of:\n", a_arr, "\nand\n", b_arr, '\n')
print (a_arr.dot(b_arr))
print (np.dot(a_arr, b_arr))
print()

