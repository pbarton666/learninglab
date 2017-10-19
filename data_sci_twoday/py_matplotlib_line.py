#py_matplotlib_line.py
import matplotlib.pyplot as plt
import pandas as pd

data=[2,8,3,6,1]
ser=pd.Series(data)
plot=ser.plot(kind='hist')  #same as ser.plot.hist()
plot.figure().show()
