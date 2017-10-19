#py_matplotlib_1.py

"A quick anatomoy of the matplotlib chart "

import numpy as np                 #python's array proccesing / linear algebra library
import matplotlib.pyplot as plt    #data visualization
from  matplotlib import rcParams   #all settable properties (reference)

#Create a np.ndarray w/ data to plot
s1=np.fromiter( [np.sin(x/10) for x in range(0, 300)], np.float)

#create a master figure container (comes with a free canvas object)
figure=plt.figure(1)            #container object
fignum=figure.number            #figure index # - only one active at a time
canvas=figure.canvas            #the canvas the figure renders into 

#add an 'axes' to hold the data 
left, bottom, width, height =   .2, .2,.6, .6  #in frac. of figure real estate
axes = figure.add_axes( (left, bottom, width, height) )

#add data (adds an entry to axes.lines list for free)
axes.plot(s1, 'blue', label='axes.plot label')

#now, you can play with properties of these objects e.g., 

#canvas
canvas.set_window_title("canvas.set_window_title")

#axes
axes.xaxis.set_label_text('axes.xaxis.set_label_text')
axes.set_ylabel('axes.set_ylabel')
axes.set_title('axes.set_title')
axes.set(label="axes.set(label=)")
axes.legend() #turns display on

#line properties
line=axes.lines[0]
line.set_marker('.')
line.set_markerfacecolor('green')
line.set_markeredgecolor('green')
line.set_label("line.set_label")

#Here are some ways to find settable properties
print(plt.setp(line))        #line properties (can be used as a setter)
print(figure.properties())   #figure properties
print(rcParams)              #a dict of all Artist properties / values

plt.show()
x=1