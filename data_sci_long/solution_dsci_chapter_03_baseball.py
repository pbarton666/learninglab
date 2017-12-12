#solution_dsci_chapter_03_baseball.py
import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt
import os

if '__file__' in dir():
    path, _=os.path.split(__file__)  
else: path=os.getcwd() 

fn=os.path.join(path, "baseball_stats.xls")
df=pd.read_excel(fn)
fig, ax=plt.subplots(nrows=2, ncols=2, figsize=(8,8))
#plt.figure(figsize=(30,30))
#fig
#plt.xticks()
ticks=[0,.1,.2,.3,.4,.5,.6,.7,.8]
ax[0,0].scatter(df['bb']/df['at_bat'], df['avg'], \
                xticks=ticks,\
                yticks=ticks)
ax[0,1].scatter(df['k']/df['at_bat'], df['avg'])


#df['bb_per_K'].bar(x=df.index)
#pitches pretty normal
#bb_per_K  lots of outliers, but pretty normal

x=1