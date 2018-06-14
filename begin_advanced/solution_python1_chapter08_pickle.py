#solution_python1_chapter08_pickle.py

import pickle
import os

"""
Please create three functions in the same module (file). Each will take two
inputs. One file will add the numbers, another will multiply and the third
will subtract them.

Destroy the three functions then recreate them from the serialized files.
Verify that they still work as well as the original ones.

You can use either json or pickle to handle the serialization.	"""

def adder(x, y):
    return x+y
def multiplier(x,y):
    return x*y
def subtractor(x,y):
    return x-y


def load_some_results():
    "function to load a test dict of results"
    x = 5;  y = 3  #you can do this, but it's not recommended
    results={'adder': adder(x, y), 
             'multiplier': multiplier(x,y),
             'subtractor': subtractor(x,y)
             }
    return(results)

#get some results
the_pickle_names=('p_adder.pkl', 'p_multiplier.pkl', 'p_subtractor.pkl')
things_to_pickle=(adder, multiplier, subtractor)  #a tuple
original=load_some_results()

#load our functions, first deleting any files already out there
for name in the_pickle_names:
    if os.path.exists(name):
        os.remove(name)

for file_name, thing in zip(the_pickle_names, things_to_pickle):
    with open(file_name, 'wb') as p:
        pickle.dump(thing, p)		

#kill them off and prove they're dead
for thing in things_to_pickle:
    thing_name=thing.__name__
    thing=None
    if thing:
        print(thing)
    else:
        print("No {} here".format(thing_name))

#bring 'em back to life	
things_to_pickle=[]
for file_name in the_pickle_names:
    with open(file_name, 'rb') as p:
        recovered_thing=pickle.load(p)
        things_to_pickle.append(recovered_thing)

#get results from them
restored=load_some_results()

#test against original
for key in original.keys():
    assert original[key]==restored[key]

#if we didn't bomb out on an AssertionError, it worked.
print("Yay!  The pickle thing worked!")
