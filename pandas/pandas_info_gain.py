"""
Classification is a way to 'bin' observations in order to better understand
particular attributes.   Optimally, observations in the same 'bin' or subset
of the original have a lot in common; and different subsets have little in common.

One measure of this is the 'information gain', or reduction of entropy (randomness)
among the observations.
"""
import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import csv

#write a file with some simple data
#the DataFrame is a 2-d object.  Think a dict of Series objects
#  or a spreadsheet.

#There are lots of ways to build one.  Here, we use a 2-d ndarray 
#  with row and column labels.

#(height, weight)
data =\
(    
(20, 10),
(30, 20),
(50, 15),
(10, 10),
(45, 35),
(60, 25),
(10, 10),
(35, 25),
(60, 25),
(70, 50)
)

#define some indices for the rows and columns
columns=('height(cm)', 'weight(kg)')   #column index
index=range(1, len(data) + 1)          #row index, starting at 1
#data
nda=np.asarray(data)  #converts an array-like object to an ndarray
#DataFrame constructor
df=pd.DataFrame(nda, index=index, columns=columns)

