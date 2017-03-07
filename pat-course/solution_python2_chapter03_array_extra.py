from array import array

#a rectangular array (easier to see what we're doing)
print("\n\n Now let's get rectangular. Element values = index")
rows=3
cols=4
index=0

#add elements
rectangular=array('i')
for row in range(rows):
    for col in range(cols):
        rectangular.insert(index,index)
        index+=1

#print it out
index=0
for row in range(rows):
    for col in range(cols):
        print("{:>5}".format(rectangular[index]), end='')
        index+=1
    print("")
print()    
        

"""
The transposed array wants these elements from the original
col=0 + row=0*cols,   col=0 + row=1*cols,   col=0 + row=2*cols
col=1 + row=1*cols,   col=1 + row=1*cols,   col=1 + row=2*cols
col=2 + row=2*cols,   col=2 + row=2*cols,   col=2 + row=2*cols
col=3 + row=3*cols,   col=3 + row=3*cols,   col=3 + row=3*cols
"""        
        
transpose=array('i')

index=0
for col in range(cols):
    for row in range(rows):
        insert_this=rectangular[col+row*cols]
        transpose.insert(index, insert_this)
        index+=1

#print out the result
index=0
trows=cols
tcols=rows
print("And the transposed version looks like:")
for row in range(trows):
    for col in range(tcols):
        print("{:>5}".format(transpose[index]), end='')
        index+=1
    print("")
print() 
