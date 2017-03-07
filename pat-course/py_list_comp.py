#py_list_comp.py

import random
values=1000
dedup = set([int(1000*random.random()) for i in range(values)])
print("we found {} duplicates!".format(len(dedup)))

#sample output (YMMV)
#we found 384 duplicates from an initial sample of 1000