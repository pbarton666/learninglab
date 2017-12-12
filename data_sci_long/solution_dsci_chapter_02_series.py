#solution_dsci_chapter_02_series.py
import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt

from solution_dsci_chapter_02_data_file import ppm

#here's the data, so we can "eyeball" it:
ppm=[317, 317, 319, 319, 320, 321, -99, 322, 323, 324, 325, 326, \
     328, 327, 329, 331, 332, 333, 334, 336, 337, 338, 340, 342, \
     343, 345, -99, 348, 349, 351, 353, 355, 356, 358, 359, 359, \
     361, 363, 364, 366, 368, 370, 371, 373, 375, 377, 380, 382, \
     384, 386, 387, 389, 392, 393, 396, 398, 401, 403, 407, 409]

#make an index with list comprehension
index = [year for year in range(1958, 2018) ]

#convert to a Series
ser=pd.Series(data=ppm, index=index)

#get rid of the bad data
ser.replace(-99, nan, inplace=True)

#use slice operations to pick off the first/last 10 values, then get the average
first_10_mean=ser[:10].mean()
last_10_mean=ser[-10:].mean()

#print stats
stg="Average CO2 {} to {}: {}"
print(stg.format(index[0], index[10], round(first_10_mean)))
print(stg.format(index[-10], index[-1], round(last_10_mean)))

#make a bar chart
plt.bar(index,ser.values)
plt.show()
