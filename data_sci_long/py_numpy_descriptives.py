#py_numpy_descriptives.py
import numpy as np
import pandas as pd
data=np.random.gumbel(size=1000)  #used for 'fat tailed' distributions


df=pd.DataFrame({'a':data, 'b':data*2})

#basic descriptives with describe()
d= df.describe()
print()
print(d)
print()
print(d['a']['mean'])
print()

#... or use min(), max(), mean(), std()
print(df.mean()['a'])
print()
print(df.min())
print()
print(df.kurtosis())
print()

from scipy import stats
dstats=stats.describe(df)
print(dstats)
print()
dstats.minmax[1][0]
print()
print(dstats.mean[0])
print()

#some tests
sn = stats.normaltest(df['a'])
print(sn)
print()
print(sn.statistic)
print()

#t-test for independent samples (are they really ind. based on distros?)
ttind= stats.ttest_ind(df['a'], df['b'])
print(ttind)
print()

#help on the t-test for related samples
help(stats.ttest_rel)



x=1