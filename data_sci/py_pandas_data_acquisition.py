#py_pandas_data_acquisition

import pandas as pd
import numpy as np
fn='test_data.csv'
with open(fn, 'w+') as f:
	f.writelines( ["c1, c2, c3\n","11, 12, 13\n", "21, 22, 23\n"])
	f.seek(0)
	for line in f.readlines():
		print(line[:-2])
print()

#use read_csv() to create a DataFrame
df = pd.read_csv(fn)
print(df)
print()
print(type(df))
print()
print(df.shape)
print()

#override the data type introspection functionality
df=pd.read_csv(fn, dtype=np.int64)
print(df)
print()

s = pd.Series(np.random.choice([3, 4, 5, 6, -9], 100))
#s=pd.Series(np.random.randint())
s.replace(-9, np.nan, inplace=True)
print(s.count())

rh=pd.Series.from_array([3, 50, -4, 99, 201])
fixed=rh[ (rh>=0) & (rh <=100)]
mask=rh.mask(((rh<0) | (rh >100)))

s.fillna()
h=s.hist()
h.figure.show()
print(df.dtypes)
pd.read_html('aaa')
help(pd.read_)
help(pd.read_sql)
help(pd.read_excel)
