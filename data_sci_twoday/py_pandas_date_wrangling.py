import os
import numpy as np              
import pandas as  pd            
import matplotlib.pyplot as plt

col_index=['c1', 'c2', 'c3']
df=pd.DataFrame([[11,12,13],[21,22,23],[31,32,33]], columns=col_index)
ef=pd.DataFrame([[1100,1200,1300],[2100,2200,2300],[3100,3200,3300]], columns=col_index)
concat=pd.concat([df, ef], axis=1)
concat.reset_index()
print(concat)


df=pd.DataFrame([[11,12,13],[21,22,23],[31,32,33]], 
                columns=col_index,
                index=[1, 2, 3])
ef=pd.DataFrame([[1100,1200,1300],[2100,2200,2300],[3100,3200,3300]], 
                columns=col_index,
                index=[2, 3, 4])
concat=pd.concat([df, ef])
concat.reset_index()
print(concat)


datafile='earthquakes.csv'

#useful if you want the directory this script is in
if '__file__' in dir():
    path, _=os.path.split(__file__)  
else: path=os.getcwd() 
    
filename=os.path.join(path, datafile)
df=pd.read_csv(filename, parse_dates=[0]) #dialect defaults to Excel

df.drop(df.columns[[5,6,7,8,9,11,12,14,15,16,17,18,20,21]], axis=1, inplace=True)
df['place']=df['place'].str.split(',').str.get(1)
df['place']=df['place'].str.strip()
df['place']=df['place'].str.replace("CA", "California")
df['year']=df['time'].dt.year
df['mon']=df['time'].dt.month
df['day']=df['time'].dt.day
#df.set_index('time', inplace=True)

pd.set_option("display.width", 100)
pt=pd.pivot_table(df, index=['place', 'year', 'mon'])

#py_pandas_combine_series.ipynb
qpoll = df.query('poll=="Quinnipiac"')
rpoll = df.query('poll=="Rasmussen Reports"')
#sort to ensure monotinic, earliest-to-latest dates
qpoll=qpoll.copy(); rpoll.copy()
qpoll.sort_index(inplace=True); rpoll.sort_index(inplace=True)
print(qpoll[:3])
print()
print(rpoll[:3])

#figure out the first and last dates
start=min(qpoll.index.min(), rpoll.index.min())
end=max(qpoll.index.max(), rpoll.index.max())

#throw in a a few days on either end (note negation in the new start offset)
padding=3  
newstart=start+pd.DateOffset(days=-padding)  
newend=end+pd.DateOffset(days=padding)

#... gin up a new date_range for the index
newix=pd.date_range(newstart, newend, freq='d')

#... apply it to both Series
qpoll=qpoll.reindex(pd.to_datetime(newix))
rpoll=rpoll.reindex(pd.to_datetime(newix))



"""
ser.rolling
autocorr()  lag  shift (latter apply to time series)
"""

from py_plotting_utils import formatPlotBar
#... specify a column to print
col_to_plot='approve'

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



#py_plotting_utils.formatPlotBar(s1=qpoll, s2=rpoll)

df.sort()