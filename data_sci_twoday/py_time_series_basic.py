#py_time_series_basic.py
import datetime

index=pd.date_range(start='1/1/2017',   periods=5, freq='d')
index=pd.date_range(start='Jan 1 2017', periods=5, freq='d')
index=pd.date_range(start=datetime.datetime(2017,1,1), \
                        periods=5, freq='d')
index=pd.date_range(start='1 Jan 2017', end='5 Jan 2017')
print(index)
print()

data=[10, 20, 30, 40]
index=pd.date_range(start='1 Jan 2017', end='4 Jan 2017')
print(index)
print()

ser=pd.Series(data=data, index=index)
print(ser)
