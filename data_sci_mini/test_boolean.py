import numpy as np
import pandas as pd

data=np.random.gumbel(size=10)  #used for 'fat tailed' distributions
t=pd.Series(data)

mean=t.mean()
stdev=t.std()
norm=(t-mean)/stdev
print(norm)
print()

bmask=norm.where(norm<1, other=np.nan)
bmask=norm.mask(norm<1, other=np.nan)
print(bmask)
print()

print('*'*30)
print('t\n', t,'\n')
print('bmask\n', bmask, '\n')
fixed= (t * bmask)
print('fixid\n', fixed, '\n')
fixed= t * bmask
fixed.hist(bins=100)
#########
t=pd.Series([1,1,2,2,2,3,3,4,5, 6])
bmask=t.where(t>3, other=0)
print()


x=1
