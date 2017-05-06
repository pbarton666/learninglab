"""Demonstration of intermediate operations employing pandas time series
      data objects and database-likeoperations; uses aggregate polling 
	  results from Real Clear Politics (http://www.realclearpolitics.com/)
"""
import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import csv
import datetime
#home-made formatting utilities
from py_utils import printme 	
from py_utils import formatPlot2, formatPlotBar

#pandas has several default output formattion options - here are a couple:
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 500)

#We could alternatively get data from a csv, Excel, SAS, etc. file w/ 
# pd.read_csv(), pd.read_excel(), pd.read_sas(), and other baked-in methods
filename='clean_polling_data.csv'
df=pd.read_csv(filename, parse_dates=True, dialect=None) #dialect defaults to Excel


#We can check on our haul in a few ways:
printme("using the info() method:", df.info())
printme("first few rows using head()", df.head(3))

#We can use the iloc() method to see a single record (row) or column
get_row=1
get_col=1
display_cols=5
printme("iloc uses integer indices")
printme("a single record:", df.iloc[get_row])   #same as df.iloc[get_row,:]
printme("a single column:", df.iloc[:,get_col][:display_cols])   
#... or the whole enchilada
printme("all polls:", df)

#we can also use the column name as a key value.  This gets all polls:
just_polls=df['poll']
print()
print('polls:' + str(type(just_polls)), 'length' + str(len(just_polls)))
#since it's a Series, we can slice the new object
printme('first five poll names:', just_polls[:5])



#Make the date the index.  The index can easily be replaced
df.set_index('date', inplace=True)
#When the date is an index be sure that data is sorted chronologically
df.sort_index(inplace=True)
printme("index is now: ", df.index.name)
printme(df.index)



#Let's say we want to look at one poll

#This searches for Gallup polls
gallup = df.query(df.poll=='Gallup')
printme("Gallup only using query()", gallup)

#... and this finds ones with a positive spread
gallup_pos=df.query("poll=='Gallup' and spread>0")
printme("Only positive spreads:", gallup_pos)

#you can combine operations against the original dataset
df.query("poll=='Gallup' and spread>0").sort_values(by=['approve', 'spread'])
#Naturally, you can sort on any column

printme('by approval rating & spread', gallup.sort_values(by=['approve', 'spread']))

#To plot multiple polls (on differnt dates) with appropriate intervals, we'll
#   want to reflect 'missing' days in the index.

#...figure out the first and last date
start=gallup.index.min()
end=gallup.index.max()

#... then create a 'date_range' object and use it as a new index
newix=pd.date_range(start, end, freq='d')

#... make sure the index is really a datetime-like object
#    NB, the 'date' column now needs to referenced as 'index'
gallup.index=pd.to_datetime(gallup.index)
gallup=gallup.reindex(newix)
printme("re-indexed dataframe looks like this:", gallup.head(15))

#We can create a 1-d time series object for plotting
gspread=gallup['spread']
title="Gallup Presidential Approval Spread"
formatPlot2(start=start, end=end, s=gspread, t=title)


########And here's how we might compare two polls
#query the original dataframe
qpoll = df.query(df.poll=='Quinnipiac')
rpoll=df.query(df.poll=='Rasmussen Reports')

#ensure the indices are datetime objects with to_datetime()
qpoll.index=(pd.to_datetime(qpoll.index))
rpoll.index=(pd.to_datetime(rpoll.index))

#... Make a chart index to include all the original dates
#       this creates datetime-like objects
start=min(qpoll.index.min(), rpoll.index.min())
end=max(qpoll.index.max(), rpoll.index.max())

#... We can manipulate these to make the chart a bit 'wider' than the index
padding=3  #(days)defaults to Days (biz days, period beginning/end available)
printme("original start:", start)
newstart=start+pd.DateOffset(days=-padding)  #defaults to Days (biz days, period beginning/end available)
printme("new start:", newstart)
newend=end+pd.DateOffset(days=padding)

#... gin up a new date_range for the index
newix=pd.date_range(newstart, newend, freq='d')

#... apply it to both Series
qpoll=qpoll.reindex(pd.to_datetime(newix))
rpoll=rpoll.reindex(pd.to_datetime(newix))

#... specify a column to print
col_to_plot='spread'

#... add some aesthetic elements
q_label ='Quinnipiac' 
q_color='b'
r_label = 'Rasmussen'
r_color='r'
title = "{} versus {} - {}".format(q_label, r_label, col_to_plot)


bar_width=2.0
opacity=.9


formatPlotBar(start=newstart, end=newend, 
              s1=qpoll[col_to_plot], s2=rpoll[col_to_plot],
              s1_label=q_label, s2_label=r_label, 
              s1_color=q_color, s2_color=r_color,
              x_label='', y_label=col_to_plot, title=title,
              bar_width=bar_width, opacity=opacity)

