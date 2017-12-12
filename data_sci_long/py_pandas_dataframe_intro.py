#py_pandas_dataframe_intro.py

import pandas as  pd            #data processing / stats library

#the DataFrame is a 2-d object.  Think a dict of Series objects
#  or a spreadsheet.  Here's one form of a constructor using a dict
#  to set up something that looks like a spreadsheet.
#  (note: we're passing info in column-wise):

data= {'c1' : pd.Series([11, 21, 31], index=['r1', 'r2', 'r3']),
       'c2' : pd.Series([12, 22, 32], index=['r1', 'r2', 'r3']),
       'c3' : pd.Series([13, 23, 33], index=['r1', 'r2', 'r3']),
     }
df=pd.DataFrame(data)
print(df)
print()

#extracting information
#   ... a column
print('column "c2":\n', df['c2'])
print()
#   ... a row
print('last row:\n', df.iloc[-1])
print()
print('using loc\n',df.loc['r3'])
print()
#   ... an element
print('element (c2, r2):',df['c2']['r2'])
print('...using at():',  df.at['r2', 'c2'])
print('...using iat():',  df.iat[1, 1])
print()

#element-wise operations
print(df/10)
print()
print(df['c1']*100)
print()

#add a new column with assign()
df.assign(c4 = df['c2']/10)
print(df)
print()

#add a new column 'manually'
df['c4']=df['c2']
print(df)
print()

#... and get rid of it
del df['c4']
print(df)
print()

#add a new column with insert()
col_index = df.columns.get_loc('c1')
new_col=pd.Series(data=[666,777,888], index=('r1', 'r2', 'r3'))
df.insert(loc=col_index, column="new", value=new_col)
print(df)
print()



#add another new column with mis-matched row indices
new_col=pd.Series(data=[666,777,888], index=('r1', 'r2', 'xxx'))
#   note dtype of new column is float (default due to NaN)
df.insert(loc=col_index, column="new1", value=new_col)
print(df)
print()

#add a row to a new DataFrame
# ... just add a non-existing row

df=pd.DataFrame(data)
row_data=(41,42,43)
df.loc['r4']=row_data
print(df)
print()

#delete the last row
df=df.drop(df.index[-1])
print(df)
print()

#get a list of row and column names
rows=df.iloc[ [0,2] ].index.tolist()
print('rows:', rows)
cols=df.columns.tolist()
print('cols:', cols)
cols=df.columns[0:2].tolist()
print('cols:', cols)
print()