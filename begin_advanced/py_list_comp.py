#py_list_comp.py

import random
values = 1000
dedup = set([int(1000*random.random()) for i in range(values)])
print("we found {} unique values!".format(len(dedup)))
