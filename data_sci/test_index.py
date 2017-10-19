import numpy as np
import pandas as pd

index = ["duck0", "duck5", "duck10"]
data= (0, 5, 10)
s=pd.Series(data=data, index=index)
print(s)
print()

#
#using slices
print(s["duck0":"duck5"])
print()
#using loc[] for "key" indices
print("duck0", s.loc["duck0"])
print()
#using iloc[] for numeric indices
print("index[1]", s.iloc[1])
print()

#index and values are separate objects
print("values", s.values)
print()
print("index", s.index)
print()

#create and apply a new Index object
newix=pd.Index(['qucker1', 'quacker2', 'quacker3'])
print(newix)
print()
s.index=newix
print(s)
print()

#re-indexing
index = ["duck0", "duck5", "duck10"]
data= (0, 5, 10)
s=pd.Series(data=data, index=index)
print(s)
print()

#   ... apply a new axis
newix=["duck0", "duck1", "duck2", "duck5", "duck10"]
newix=("duck0", "duck1", "duck2", "duck5", "duck10")
s= s.reindex(newix)
print(s)
print()

#fill in values
print (s.ffill())
print()

#sorted versions
print(s.sort_index())
print()
print(s.sort_values())
print()