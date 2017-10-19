#py_python_basics_for_ds.py

ls=[]    #an empty list

ls=[1, 2.4, 'hey', {'a':1, 'b':2}]
print(ls, '\n')

ls=list(range(10))
print(ls, '\n')
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                
print(ls[3] , '\n')                 
print(ls[0:5], '\n')    #a contiguous block          
print(ls[0:5:2] , '\n') #every second element              
print(ls[-1] , '\n')    #last element               
print(ls[-2] , '\n')    #second-last element

#slice objects
slc=slice(0, 5, 2)
print(ls [slc], '\n')

#adding objects
ls=list(range(3, 10, 2))
print(ls)
print()

ls.append(777)
print(ls)
print()

ls.extend('abc')
print(ls)
print()

index=0
ls.insert(index, '-34')
print(ls)
print()

ls.insert (ls.index(777), 888)
print(ls)
print()


#removing elements
ls = ['dog', 'pony', 'unicorn']
my_little = ls.pop(1)
print('popped: {}.  list now): {}'.format(my_little, ls))
ls.remove('unicorn')

#sort
#list of lists

#np - insert rows, columns

#dict objects
the_dict = {"key":"value", "A":2, "B":3}
same_dict = dict(key="value", A=2, B=3)
print("Dict compare    :", the_dict == same_dict)
print("And here's the dict:", the_dict)
print()

#adding elements
the_dict['C']=3
print("... and again:", the_dict)
print()
the_dict.update( ( ('a', 100), ('b', 200) ))
print("... and again:", the_dict)
print()

#removing elements
val = the_dict.pop('A')
print("{} returned; dict now: {}".format(val, the_dict))
print()
val=the_dict.popitem()
print("{} returned; dict now: {}".format(val, the_dict))
print()
if 'a' in the_dict:
	del the_dict['a']
print(the_dict)
print()

#retrieving an object by key when you're not sure if key exists
val = the_dict.get('zebra')
print(val)
val = the_dict.get('zebra', 'default_value')
print(val)
print()


#comprehensions

#list comprehension
#[                ]  # square brackets
#[  for i in range(5)  ]  #add an iterating expression
#[ 'xxx'  for i in range(5) ]  # add something to put in the list

comp=[ 'xxx'  for i in range(5) ]
print(comp)
print()
comp=[ i**3  for i in range(5) ]
print(comp)
comp=[ i**3  for i in range(5) if i%2 and i>1]
print(comp)
print()
comp=[  j[0:2] for j in [ 'xxx'  for i in range(5) ]  ]
print(comp)
print()
comp=[  k[0] for k in [  j[0:2] for j in [ 'xxx'  for i in range(5) ]]]
print(comp)
print()
comp=[m+"Y" for m in [k[0] for k in [  j[0:2] for j in [ 'xxx'  for i in range(5) ]]]]
print(comp)
print()

#dict comprehension
comp={  i:i**2  for i in range(5) }
print(comp)
comp={  "new_key"+str(key):val**3  for key, val in {  i:i**2  for i in range(5)}.items()    }
print(comp)
print()

#middleware libraries
import os
#relative path
mypath= os.path.join("tools", "image_processing")
print(mypath)
print()
#extended path
abspath=os.path.abspath(mypath)
print(abspath)
print()
#file name
filename=os.path.basename(mypath)
print(filename)
#separate extension from file name
print(os.path.splitext(mypath))
print()

#navigate
print("directory is now:", os.getcwd())
os.chdir('..')
print("directory is now:", os.getcwd())
print()

#create new directory
import random
fn='junk'+str(random.random())
os.mkdir(fn)
os.chdir(fn)
print("directory is now:", os.getcwd())
open('junkfile', 'w').close()
print(os.listdir())

#get info about user, objects
print(os.getuid())  #process userid
print(os.stat('junkfile'))  #file metadata
print()

#os-related tools from sys
import sys
try:
	print(sys.getwindowsversion)
except: pass
print()
print(sys.platform)
print()
print(sys.stdout)
print()
print(sys.getfilesystemencoding)
print()
print(sys.thread_info)
print()