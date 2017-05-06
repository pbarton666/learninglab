"""First-order exploration of pandas Series object"""

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import matplotlib.dates as dates
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities

live=False

#Create some data to be used in a time series
data=[10, 20, 30, 40]

#Here's how to create a pandas Series object:
ser=pd.Series(data=data)
printme("Let's have a look:", "index  value", ser)

#Slicing operations are supported - you get an index "for free"
printme('second value only is:', ser[1])
printme('a slice from position 1 to 3:', ser[1:3])

#Like a list, values can be heterogenous objects:
ser[0]='some string'  
ser[1]=(1,2,3)
ser[55]=5555555
printme(ser, '\n')

#we can remove and retrieve objects using pop() on the index
value_3=ser.pop(3)
value_5=ser.pop(55)
print('value_3:  {}'.format(value_3))
print('value_5:  {}'.format(value_5))
printme(ser)

#get() is also supported
default=ser.get(666, "nope")
printme(default)

#We can use the keyword 'in' to test indices
look_for= 0
result=look_for in ser
printme('Is {} in the series?  {}'.format(look_for, result))
printme()


#We can find values using the isin() method of Series
print('isin() produces a boolean mask; the argument is a list\n')
look_for=[ (1,2,3) ]
print('looking for', look_for)
printme(ser.isin( look_for ))

look_for=[ (1,2,3), 30, 50]
printme('looking for', look_for)
printme(ser.isin( look_for ))



#Better indices ... pandas work and play well with dates

#Create an index object (DatetimeIndex) for the time series
#   - Anything that looks like a date works. Default is range(len(data))
#   - Optional arguments can localize/normalize to 2400: 
#         tz='America/Los_Angeles', normalize=True
#   - Frequencies can be ms, s, m, h, d, a <several flavors of a (annual)>
#       a-dec, a-mar, etc. For offset from specific day: pd.DateOffset(years=2)

#These all produce dates from Jan 1, 2017 - Jan 5, 2017
import datetime
data=[10, 20, 30, 40]
index=pd.date_range(start='1/1/2017',   periods=4, freq='d')
index=pd.date_range(start='Jan 1 2017', periods=4, freq='d')
index=pd.date_range(start=datetime.datetime(2017,1,1), periods=4, freq='d')
index=pd.date_range(start='1 Jan 2017', end='4 Jan 2017')

printme("Here's our index:")
printme(index)

#We can load our data and index into a Series object in one fell swoop
data=[10, 20, 30, 40]
index=pd.date_range(start='1 Jan 2017', end='4 Jan 2017')
ser=pd.Series(data=data, index=index)
printme("... and here's our series:")
printme(ser)

#It's easy top operate on the entire index or data vector:
#   advance index by a day and increment each value
printme("first date:  {}  first value: {}".format(ser.index[0], ser[0]))
ser.index=ser.index+1
ser=ser+100
printme("now, check it out:", ser)

#We can shift it out a couple years if we want
add_years=2
ser.index=ser.index+ pd.DateOffset(years=add_years)
printme("extended {} years:".format(add_years))
printme(ser)

#pandas has lots of built-in 'intelligent dates'
from pandas.core.datetools import BYearEnd, Easter, QuarterEnd, BMonthEnd
new_year=pd.datetime(2017, 1, 1)
easter= pd.date_range(start=new_year,periods=3, freq=Easter())
printme('Happy Easter!', easter)
qend=pd.date_range(start=new_year, periods=4, freq=QuarterEnd())
printme("End of quarters:", qend)


#Plotting can be super-easy with matplotlib (but it's ugly)
plt.plot(ser)
if live: plt.show()

#Tease out 'figure' and 'axes' objects to apply formatting
fig, ax = plt.subplots()

#add the Series object (we could add x and y values separately)
ax.plot(ser)

#to apply axes formatting, create and apply a formatting object
x_format = dates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(x_format)

#this automatically 'slants' the text so it's legible
fig.autofmt_xdate()

#this 'pads out' the chart with a little extra margin
plt.tight_layout()

#we can optionally add a title
plt.title("The most boring plot ever - bigly")

#this renders the plot
plt.show()
a=1
