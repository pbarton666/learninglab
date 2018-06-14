#py_dict_1.py
mydict={}
mydict['team'] = 'Cubs'

#another way to add elements us via update().  For input, just about
#   any iterable that's comprised of  2-element iterables will work.

mydict.update([('town', 'Chicago'), ('rival', 'Cards')])

#we can print it out using the items() method (it returns a tuple)

for key, value in mydict.items():
    print("key is {} and value is {}".format(key, value))

print("let's get rid of a rival")
print()

#and evaluates left to right; this protects from crashes if no 'rival' 

if "rival" in mydict and mydict['rival'] == 'Cards':
    #note that del is NOT a dict method
    del(mydict['rival'])
print()

print("by the grace of a top-level function, the Cards are gone:\n")   






