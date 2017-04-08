import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import csv

#the DataFrame is a 2-d object.  Think a dict of Series objects
#  or a spreadsheet.  Here's one form of a constructor using a dict
#  to set up something that looks like a spreadsheet.
#  (note: we're passing info in column-wise):

data= {'c1' : pd.Series([11, 21, 31], index=['r1', 'r2', 'r3']),
       'c2' : pd.Series([12, 22, 32], index=['r1', 'r2', 'r3']),
       'c3' : pd.Series([13, 23, 33], index=['r1', 'r2', 'r3']),
     }
df=pd.DataFrame(data)

x=1
"""
>>> df
    c1  c2  c3
r1  11  12  13
r2  21  22  23
r3  31  32  33
"""
#
#we can extract a column using it's key, or an element coupling w/ row index
#
"""
>>> df['c2']
r1    12
r2    22
r3    32
Name: c2, dtype: int64

>>> df['c2']['r2']
22
"""
#
#DataFrames support element-wise scalar operations on the whole 
#  object or just parts of it
#
"""

>>>df/10
     c1   c2   c3
r1  1.1  1.2  1.3
r2  2.1  2.2  2.3
r3  3.1  3.2  3.3

>>> df['c1']*100
r1    1100
r2    2100
r3    3100
Name: c1, dtype: int64
"""

#
#columns can be added with newly-computed values, if desired. Note
#  that columns are added to a new copy of the df (assignment required
#  to make changes permanent).
#
"""
>>> df.assign(c4 = df['c2']/10)
    c1  c2  c3   c4
r1  11  12  13  1.2
r2  21  22  23  2.2
r3  31  32  33  3.2

>>>df
    c1  c2  c3
r1  11  12  13
r2  21  22  23
r3  31  32  33
"""

#DataFrame objects can be manipulated easily, in much the same way
#  ndarray objects can.  For instance:
#
#Transposition
#
"""
>>>df.T
    r1  r2  r3
c1  11  21  31
c2  12  22  32
c3  13  23  33
"""
#
#DataFrames also work and play well with numpy element-wise
#   universal functions "ufuncts". These include:  mod, 
#   log (natural log), add, multipy, etc.  A full list is here:
#   https://docs.scipy.org/doc/numpy/reference/ufuncs.html
#
"""
>>> np.add(df, df.T)
    c1  c2  c3
r1  22  33  44
r2  33  44  55
r3  44  55  66
"""
#
#One can plot data using the DataFrame plot() method - or matplotlib, etc.
#Here's a simple scatter plot expression:
#
"""
>>> df.plot(kind='scatter', x='c1', y='c2')
<matplotlib.axes._subplots.AxesSubplot object at 0x7f8dc4106080>
"""
#
#It's possible to make database-like queries
#
"""
>>> df.query('c1 > 30.3')
    c1  c2  c3
r3  31  32  33
"""




