#py_pandas_series_1.py
"""a first look at pandas"""

#creating a series
import pandas as  pd 
data=[10, 20, 30, 40]
ser=pd.Series(data=data)
print(ser)
print()

#addressing elements
ser[0]='some string'  
ser[1]=(1,2,3)
print(ser)
print()

#managing elements
value_3=ser.pop(3)
print(value_3)
print()

print(ser.get(666, 'nope'))
print()

print(ser)
print()

#searching   in versus isin()
print(2 in ser)
print(666 in ser)
print()
look_for=[ (1,2,3), 30, 50]
ser.isin(look_for)
print()
print(ser.isin( [0] ))
print(ser.isin( (1,) ) )
print()

###managing indices
data=[10, 20, 30, 40]
ser=pd.Series(data=data)
print(ser.index)
print()
ser.index=('dog', 'cat', 'bear', 'anteater')
print(ser.index)
print(ser.iloc[1])
print()

x=1

#quick and dirty plotting
import matplotlib.pyplot as plt #data visualization
data=[10, 20, 30, 40]
ser=pd.Series(data=data)
fig, ax = plt.subplots()
ax.plot(ser)
plt.show()
z=1


