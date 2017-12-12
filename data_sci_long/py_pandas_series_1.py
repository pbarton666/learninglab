#py_pandas_series_1.py
import pandas as  pd 
from numpy import nan

#set up a Series with some data
data=[10, 20, 30, 40]
ser=pd.Series(data=data)
print(ser)
print()

#manipulate values
ser[0]='some string'  
ser[1]=(1,2,3)
print(ser)
print()

#remove and return a value
print(ser.pop(3))
print()

#use get() for fail-safe attempt to return a value
ser.get(666, 'nope')
print(ser)
print()

#snag the values or index
print(ser.values.__repr__())
print()
print(ser.index.tolist())
print()

#discover if values exist
print(2 in ser)
print()

print(666 in ser)
print()

#discover if multiple values exist
look_for=[ (1,2,3), 30, 50]
print(ser.isin(look_for))
print()

print(ser.isin( [0] ))
print(ser.isin( (1,) ))    #a one-element tuple
print()

#replace values
ser = pd.Series([100, 110, 0,  115])
ser.replace(0, nan, inplace=True)
print(ser)
print()

#create a new Series with a default index
data=[10, 20, 30, 40]
ser=pd.Series(data=data)
print(ser.index)


#upgrade the index
ser.index=('dog', 'cat', 'bear', 'anteater')
print(ser.index)
print()

#find values using the new index
print(ser['dog'])
print(ser.iloc[2])

