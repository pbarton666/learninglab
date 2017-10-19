#py_panda_panel.py
"""3-d pandas objects"""
import pandas as pd
import xarray as xr

data= {'c1' : pd.Series([11, 21, 31], index=['r1', 'r2', 'r3']),
       'c2' : pd.Series([12, 22, 32], index=['r1', 'r2', 'r3']),
       'c3' : pd.Series([13, 23, 33], index=['r1', 'r2', 'r3']),
       }

#make a couple DataFrames
df1=pd.DataFrame(data)
df2=df1+100

print(df1)
print(df2)
print()

#... roll them up into a dict, thence into a Panel
p_dict={"Frame1": df1, "Frame2": df2}
pan=pd.Panel(p_dict)
print(pan)
print()

#here's one of the frames
print(pan['Frame2'])

#longitudinal slices:
#     minor (row) axis:
pan.minor_xs(pan.minor_axis[1])
#     major (column) axis:
pan.major_xs(pan.major_axis[1])
#

#convert to xarray   
#    a single Series
xarr_Series=xr.DataArray(df1['c1'])
print(xarr_Series)
print()

#    a DataFrame    reverse operation:   xarr_Series.to_pandas()
xarr_DataFrame=xr.Dataset(df1)
print(xarr_DataFrame)
print()

#    an intact Panel reverse operation:   xarr_Panel.to_pandas()
xarr_Panel=xr.Dataset(pan)
p=xarr_Panel
print(xarr_Panel)
print()

#explore a DataSet
fr=xarr_Panel.coords
print(fr)
print()


#print()
x=1
