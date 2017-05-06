import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import scipy
import matplotlib.pyplot as plt #data visualization
import seaborn as sns
import matplotlib.dates as dates #date munging
import csv
import datetime
import math
from py_utils import printme 	#home-made formatting utilities

live=False  #set True to show plots; False to supress

# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
#from imutils import paths
#import numpy as np
#import argparse
#import imutils
#import cv2
#import os


file_name='iris.data.csv'  #Fisher's classic

#create a DataFrame object
df=pd.read_csv(file_name)
iv_names=['slength', 'swidth', 'plength', 'pwidth']
dv_name='iclass'

iv_data = X= df[iv_names].values
dv_data= y = df[dv_name]

knc=KNeighborsClassifier(n_neighbors=3)
knc.fit(iv_data, dv_data)
a=1
"""

>>> neigh = KNeighborsClassifier(n_neighbors=3)
>>> neigh.fit(X, y) # doctest: +ELLIPSIS
KNeighborsClassifier(...)
>>> print(neigh.predict([[1.1]]))
[0]
>>> print(neigh.predict_proba([[0.9]]))
[[ 0.66666667 0.33333333]]
"""