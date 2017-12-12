#py_matplotlib_1.py

import numpy as np              #python's array proccesing / linear algebra library
import matplotlib.pyplot as plt #data visualization
import matplotlib.dates as dates

red='r'; blue='b'; green='g'; greenish='chartreuse'; magenta='m';black='b'
circle='o'; x='x';

#set this to True to show all the plots; False for dev/debugging
live=True

#Whistle up a sin and cos to plot
sin=numpy.ndarray([np.sin(x/10) for x in range(0, 300)])
cos=numpy.ndarray([np.cos(x/10) for x in range(0, 300)])


