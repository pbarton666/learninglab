#pandas_cluster_1

"""exploration classical 1936 R.A. Fisher dataset, demonstrates application of
   pandas and scikit-learn.  This module focuses on visualizing information with
   matplot lib.  Data courtesy of:  
   http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names

	                                
"""

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import seaborn as sns
import matplotlib.dates as dates #date munging
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities

live=False

file_name='iris.data.csv'
"""Data characterizes length and width of sepals and petals of Iris types.
   First couple of lines are:
      slength, swidth, plength, pwidth, class
	  5.1,3.5,1.4,0.2,Iris-setosa
"""
#create a DataFrame object
df=pd.read_csv(file_name)  

#let's have a quick look
printme('First few lines:', df.head())
printme('Extract a row using iloc();  ix() also works)')
line50=df.iloc[50]
printme(line50)
sepal_width_50=line50['swidth']
printme("Here is the 50th sepal width:  ", sepal_width_50)

#you can use info() to look at the firlds
printme(df.info())

#this uses describe() to create descriptive statistics
printme(df.describe())
print()

#Have a look at the unique categorical values of the iris types
#      pd.Categorical.from_array() provides 'one stop shopping'  

auto_cats=pd.Categorical.from_array(df['iclass'])
print(auto_cats.describe())

#This adds a new DataFrame column w/ category designations
df['iclass_ix']=auto_cats.codes

#Let's visualize the data so we can get our arms around it
#  a bit better.

#have a look at sepal / petal length scatter using pandas plot() method
ax=df[df.iclass=='Iris-versicolor'].\
         plot.scatter(x='slength', y='swidth', 
                      color='yellow', label='versicolor') 
                 
df[df.iclass=='Iris-setosa'].\
          plot.scatter(x='slength', y='swidth', 
                       color='red', label='setosa',
                       ax=ax)

df[df.iclass=='Iris-virginica'].\
          plot.scatter(x='slength', y='swidth', 
                       color='blue', label='virginica', 
                       ax=ax)

ax.set_title("scatter") 

if live: 
	ax.figure.show()

#You can also "throw the spaghetti against the wall" and look
#  at all the scatters and some summary data:
if live:
	pd.tools.plotting.scatter_matrix(df)

#... and make it even prettier using seaborn (an alternative plotting
#    library).
if live:
		sns.set()
		sns.pairplot(df[['slength', 'swidth', 'plength', 'pwidth', 'iclass']],
					 hue="iclass", 
		             diag_kind="kde")
		sns.plt.show()
		

