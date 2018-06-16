#py_matplotlib_1.py

"""Creates a plot labeled with internal object names for easy reference."""

import numpy as np              #python's array proccesing / linear algebra library
import matplotlib.pyplot as plt
from matplotlib import rcParams  #settable properties

s1 = np.fromiter(  [np.sin(x/10) for x in range(0,300)], np.float)

#create a master figure container (comes with a free canvas object)
figure = plt.figure(1)       #container object
fignum = figure.number       #figure index # - one active at a time
canvas = figure.canvas       #the canvas the figure renders into

left, bottom, width, height = .2, .2, .6, .6
axes = figure.add_axes(  (left, bottom, width, height)  )

#add data (adds an entry to axes.lines list for free
axes.plot(s1, 'blue', label = 'axes.plot label')

#canvas
canvas.set_window_title("canvas.setwindow_title")

#axes
axes.xaxis.set_label_text('axes.xaxis.set_label_text')
axes.set_ylabel('axes.set_ylabel')
axes.set_title('axes.set_title')
axes.set(label = "axes.set(label = )")
axes.legend()  #turns display on

#line properties
line = axes.lines[0]
line.set_marker('.')
line.set_markerfacecolor('green')
line.set_markeredgecolor('green')
line.set_label('line.set_label')

figure.show()

#show settings
print(plt.setp(line))          #line properties
print(figure.properties())    #figure properties
print(rcParams)               #a *huge* dict of Artist settable properties




