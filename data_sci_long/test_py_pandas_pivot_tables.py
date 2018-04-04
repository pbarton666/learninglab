#py_pandas_pivot_tables.ipynb
import numpy as np              
import pandas as  pd            
import matplotlib.pyplot as plt 
#%matplotlib inline
import os
datafile='earthquakes.csv'

#useful if you want the directory this script is in
if '__file__' in dir():
	path, _=os.path.split(__file__)  
else: path=os.getcwd() 

filename=os.path.join(path, datafile)
df=pd.read_csv(filename, parse_dates=[0]) #dialect defaults to Excel

#py_pandas_pivot_tables.ipynb

#use time for the index
df['place']=df['place'].astype(str)
df['place']=df['place'].str.split(',').str.get(1)
df['place']=df['place'].str.strip()
df['place']=df['place'].str.replace("CA", "California")

#  make year, month, and day columns
df['year']=df['time'].dt.year
df['mon']=df['time'].dt.month
df['day']=df['time'].dt.day

#nuke extraneous columns
df.drop(df.columns[[1,2,5,6,7,8,9,11,12,14,15,16,17,18,20,21]], \
        axis=1, inplace=True)

#make time the index
df.set_index('time', inplace=True)

df.head(3)