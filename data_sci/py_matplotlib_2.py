#py_matplotlib_2.py

import numpy as np            
import matplotlib.pyplot as plt
import seaborn as sns

s1=np.fromiter( [np.sin(x/10) for x in range(0, 300)], np.float)
s2=np.fromiter( [np.sin(x/5 + 50) for x in range(0, 300)], np.float)

plt.figure()
g=sns.regplot(x=s1, y=s2,  color="m")
plt.show()
x=1