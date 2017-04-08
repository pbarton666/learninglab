import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import csv

#the Series object (a 1-d array - a "list/dict on steroids")

#simplest case - data is scalar
#
data = 5                      #array-ish, scalar, or n-dimension array (ndarray)
index=['some value']          #array-ish collection, same length as data
s = pd.Series(data, index)    #index is optional - if not provided, ints from zero)
"""
>>> s
some value    5
dtype: int64
"""

#
#data can be array-ish e.g., a list, elements can be anything
#index elements need to be hashable and unique
#
data=["aye",     'bee',    123, complex(1,2)]
index=['thing1', 'thing2', 123, 'c']
s = pd.Series(data, index)
"""
>>> s
thing1       aye
thing2       bee
123          123
c         (1+2j)
dtype: object
"""

#
#to extract an element, use slice syntax
#
"""
>>> s['thing1']
'aye'
"""

#
#data can also be a dict - keys automatically become the index
#
data={'team': 'Cubs', 'town': 'Chicago', 'beer':'Old Style'}
s = pd.Series(data)
"""
>>> s
beer    Old Style
team         Cubs
town      Chicago
dtype: object
"""

#it's possible to slice by keys:
"""
>>> s['beer':'team']
beer    Old Style
team         Cubs
dtype: object
"""

#values accessible by keys or index values (elements are auto-sorted)
"""
>>> s[2]
'Chicago'
>>> s['town']
'Chicago'
"""

#
#valid operators are applied as scalar operations
#
"""
>>> s*2
beer    Old StyleOld Style
team              CubsCubs
town        ChicagoChicago
dtype: object
"""

#
#a Series can be created from a ndarray:
#
nda=np.zeros([3,])  #one-d ndarray object w/ 3 elements
s=pd.Series(nda)

"""
>>> s
0    0
1    0
2    0
dtype: float64
"""
x=1