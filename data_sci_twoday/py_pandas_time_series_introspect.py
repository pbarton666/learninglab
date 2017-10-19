#py_pandas_time_series_introspect.py

"""Demonstration of intermediate operations employing pandas time series
      data objects and database-like operations; uses aggregate polling 
	  results from Real Clear Politics (http://www.realclearpolitics.com/)
"""
import pandas as  pd            #data processing / stats library
import os

#pandas has several default output formattion options - here are a couple:
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 500)

path, _=os.path.split(__file__)  #find path this script lives on
filename=os.path.join(path, 'clean_polling_data.csv')
df=pd.read_csv(filename, parse_dates=[0], dialect=None) #dialect defaults to Excel


#We can check on our haul in a few ways:
df.info()
df.head(3)

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
