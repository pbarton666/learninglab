import numpy as np 
import pandas as pd

t=np.array([1,2,3])
u=np.array([1,np.NaN,3])
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['A', 'Z', 'C', 'Y', 'E'])

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=[1, (1,2,3), 'C', 'Y', 'E'])
x=1