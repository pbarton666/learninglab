
#py_dict_exotics.py

"demonstrates the use of the defaultdict and OrderedDict"

from collections import defaultdict

#defaultdict takes some sort of callable as an argument
dd = defaultdict(int)   #when int is called, it returns 0
for animal in ('dog', 'cat', 'dog', 'zebra'):
	dd[animal] +=1
print(dd)


#You can "roll your own" callable.  
def callable_constant_factory(value_if_missing):
	#This lambda (anonymous function) returns what to use for a devault value
	return lambda : value_if_missing  

#loads the callable up with the value we want (can be anything)
dd = defaultdict(callable_constant_factory("default_value"))

for animal in ('dog', 'cat', 'dog', 'zebra'):
	print("key: {}, value: {}".format(animal, dd[animal]))

print("\nkeys:\n{}".format(dd.keys()))
print()

#The OrderedDict works just like a dict
from collections import OrderedDict

od = OrderedDict()
print(od)
print()
od.update( ( ('dog', "Quinn"), ('cat', "Barfy"), ('fish', 'Jaws')))
print("The value of {} is {}.".format('dog', od['dog']))
print()
print("adding a new value for 'dog'")
od['dog'] = "Fang"
print()

print("Our OrderedDict is now:")
for k, v in od.items():
    print(k, v)

z = 1