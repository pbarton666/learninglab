import numpy as np     
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
s1=pd.Series([1,2,4,5,6,7,8,7])
mu, sigma = stats.norm.fit(s1)  #mean, standard deviation
ax=sns.distplot(s1, kde=False, fit=stats.norm)
plt.title="Check against normal distribution"
plt.legend("normal ($\mu=${0:.2g}, $\sigma=${1:.2f})".format(mu, sigma))
ax.legend("normal ($\mu=${0:.2g}, $\sigma=${1:.2f})".format(mu, sigma))
plt.ylabel("frequency")
plt.xlabel("observation")


s1=np.fromiter( [np.sin(x/10) for x in range(0, 300)], np.float)
s2=np.fromiter( [np.sin(x/5 + 50) for x in range(0, 300)], np.float)

g=sns.regplot(x=s1, y=s2,  color="m")
g.figure.show()

import pandas as pd
s1 = pd.Series([np.random.randint(0,100) for x in range(100)])
boxplot=s1.plot.box()
x=1

