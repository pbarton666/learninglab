#py_nested_list.py

"how to use lists like arrays"
one=[11, 12, 13]
two=[21, 22, 23]
three=[31, 32, 33]

#make a list of lists
arr=[one, two, three]

print(arr)

row=1
col=2

print("The value of the element of row {}, col {} is {}"\
      .format(row, col, arr[row][col]))


