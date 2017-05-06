"""Introduction to DataFrames - 2d panda objects"""

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import matplotlib.dates as dates
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities

live=False


#One can begin with Series objets ...
s1=pd.Series([np.sin(x/10) for x in range(0, 300)])
s2=s1.copy()
s2.index=s2.index-50
s3=s1*2
s1=pd.Series([np.cos(x/10) for x in range(0, 300)])

#... and load them into a data frame
df = pd.DataFrame(s1)
df['s2']=s2
df['s3']=s3

#... which provides built-in plotting capability
#    NB, the syntax is different than straight matplotlib
bar=df.plot.bar()
bar.xaxis.set_label_text("hey there!")
bar.set_title("Who thought trig could be cool?")
bar.figure.show()

#we can then plot individual series simply
df[0].plot(kind='bar')
plt.axhline(0, color='r')