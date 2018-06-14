#py_files_5.py
import pickle as pickle
from junk import JUNK

pickle_file="dill"
#make a couple objects
obj = [ [1, 2, 3],
        [4, 5, 5],
        [7, 8, 9]
        ]
obj1="howdy doody"
obj2=set([33,43,53])

#another (better) way:
to_pickle={'obj' : obj,
           'obj1': obj1,
           'obj2': obj2,
           'junk': JUNK
           }
with open(pickle_file, 'wb') as f:
    pickle.dump(to_pickle,f)

to_pickle=None

with open(pickle_file, 'rb') as f:
    to_pickle=pickle.load(f)

for k, v in to_pickle.items():
    print(k,v)		  