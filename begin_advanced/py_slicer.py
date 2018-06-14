#py_slicer.py
the_string = "strings are sequences with an encoding"
the_list=list(range(0,10))
the_slice = slice(3, 10) # positions 3...9 inclusive
print("Slice       : ", the_slice)
print("Slice a list: ", the_list[3:10])  # more typical
print("Alt. syntax : ", 
      the_list.__getitem__(the_slice))    # more verbose


print("Slice a string: ", the_string[3:10]) # slice a string
print("The whole string: ",the_string[:])   # "the whole enchilada"
print("Skipping: ",the_string[::2])         # step by 2
new_list = the_list[:]     # same as the_list.copy()




