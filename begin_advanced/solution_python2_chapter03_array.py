#solution_python2_chapter03_array.py

from array import array
#create a new array
rows=3 
cols=3 
index=0 

new_arr=array('i')
#Create an array and print it out
for row in range(rows):
    for col in range(cols):
        new_arr.insert(index,row*10+col)
        index+=1


#print(new_arr) 
#array('i', [0, 1, 2, 10, 11, 12, 20, 21, 22])
#
#            -row_0-   --row_1--  --row_2--
#index vals: 0  1  2   3   4   5   6   7   8
#
# first column:  0,  0+rows, 0+rows*2
# second column: 1,  1+rows, 1+rows*2
# second column: 2,  2+rows, 2+rows*2

#In above example, if we start with the index value of the column we're
#  after in the first row, we can "stride" by <rows> to get the rest
#  of the values in that column

#If we started with index of the first element of the row we're after, we
#  can stride by <columns> to pick up the rest.

#for a dict comprehension, we need two iterables.  Let's make them
keys=range(cols)
values=[]
for key in keys: #gin up a tuple of tuples
    values.append((new_arr[key],
                   new_arr[key+rows], 
                   new_arr[key+rows*2])
                  )
iterable_of_key_value_pairs=zip(keys, values)

#now we can snag our (key, value) pairs from 
col_dict={ key: value for key, value in iterable_of_key_value_pairs}
#... and print it out
print(col_dict)
