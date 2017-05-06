#read a csv file, loading it into a DataFrame

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import csv

#read in some data
fn = 'polling_data.csv'
df=pd.read_csv(fn)

#we can manually sets print options (lots of stuff like precision, max_colwidth avail)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 5)

print("Here's what our data looks like:\n")
print(df.head(n=4))

#these are the indices auto-loaded:
print('\n')
print('row index:')
print(df.index)
print('\ncolumn index:')
print(df.columns)

print('\ncheck out the data types:')
pd.set_option('display.max_rows', 10)
print(df.dtypes)

#to select one or more columns, use slice notation
print('\n')
print(df["Datetime"])

#note that Datetime is not right (it came from Excel).  Here's a fix:
df=df.assign(Datetime=pd.to_datetime('1899-12-30') + pd.to_timedelta(df['Datetime'], 'D'))
#df.pop("Datetime")

print('\nMake sure it "took":')
pd.set_option('display.max_rows', 11)
print(df.dtypes)

print('\nThe first few lines of data:')
print(df.head())

print('\nWe can search for a specific value')
print("check for Quinnipiac")
print("SQL equivalent:  SELECT * WHERE Poll=Quinnipiac")
q=df.loc[df["Poll"]=="Quinnipiac"]
print(q)
print()
print("check for Quinnipiac or Rasmussen")
print("SQL equivalent:  SELECT * FROM <df> WHERE Poll=Quinnipiac OR Poll='Rasumssen Reports")
q=df.loc[df["Poll"].isin(["Quinnipiac", "Rasmussen Reports"])]
print(q)

print("\nWe can also sort the data.")
print("Note that we apply SQL equivalent to '... ORDER BY Poll, Datetme' separately.\n")
qsort=q.sort_values(["Poll", "Datetime"])
print(qsort)

print("\nWe can plot it out in various formats")
q=df.loc[df["Poll"]=="Quinnipiac"]
qsort=q.sort_values(["Poll", "Datetime"])
chart=qsort.plot.bar(x="Datetime", y="Spread")
fig=chart.get_figure()
#fig.show()

print("\n... and save it  ")
fig.savefig("test.png")

#note: after creation, you can review the settings by accessing
#  properties like fig.get_edgecolor() and change them with
#  methods like fig.set_edgecolor()


fn = 'polling_data.csv'
df=pd.read_csv(fn)

#create a real datetime column
df=df.assign(Datetime=pd.to_datetime('1899-12-30') + pd.to_timedelta(df['Datetime'], 'D'))

#create a nice, human-readable version of the date
df["DatetimeH"]=df["Datetime"].dt.strftime("%Y-%b-%d")

#define selection and sort criteria
q=df.loc[df["Poll"]=="Quinnipiac"]
qsort=q.sort_values(["Poll", "Datetime"])

#create a plot object and display it
chart=qsort.plot.bar(x="DatetimeH", y="Spread")
#this sets the horizontal axis; color is RGBA, values between 0 and 1
chart.axhline(.5, color='k', linewidth=1)
#this provides larger exterior margins

fig=chart.get_figure()
fig.set_tight_layout(True)

fig.show()

#=============================
qsort=df.sort_values(["Datetime"])
qsort.index=qsort["Datetime"]
#create a plot object and display it
chart=qsort.plot.bar(x="DatetimeH", y="Spread")
#this sets the horizontal axis; color is RGBA, values between 0 and 1
chart.axhline(.5, color='k', linewidth=1)
#this provides larger exterior margins

fig=chart.get_figure()
fig.set_tight_layout(True)

fig.show()
x=1

