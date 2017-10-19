#py_matplotlib_subplots.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(10, 3), columns=['c1', 'c2', 'c3'])
fig, ax= plt.subplots(nrows=2, ncols=2)
a=ax[0][0]
df.plot.bar()
df.plot.barh(stacked=True)