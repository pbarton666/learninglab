#py_pandas_plot.py
import pandas as pd

ser=pd.Series([2,8,3,6,1])
plot=ser.plot(kind='hist')  #same as ser.plot.hist()
#plot.figure().show()
x=1