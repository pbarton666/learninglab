import os
import pandas as pd
from openpyxl import load_workbook

data_dir = "."
template = 'chartme_template.xlsx'
new_wkbk = 'chartme_data_added.xlsx'
tab_name = 'data'

ROWS_AXIS = 0
COLS_AXIS = 1

def normalize(series):
    """Accepts a column (a pandas.Series object) and returns a normalized
          version.  Operations are applied to all elements of the column.
          'Normalized' means centering its distribution."""
    mean = series.mean()
    sdev = series.std(ddof = 0)  #population standard dev
    normalized = (series - mean) / sdev
    return normalized

def element_wise_operations(df, col0, col1, axis = ROWS_AXIS):
    """Accepts a DataFrame and applies element-wise operations.   Operations """

def create_data():
    """Creates and returns a DataFrame"""
    data = \
        [
          ['baseball', 180, 1100],
          ['wrestling', 30,  300],
          ['gymnastics', 1,  120],      
        ]
    cols = ['sport', 'duration', 'fans' ]
    
    sports_df = pd.DataFrame(data=data, columns=cols)
    
    return sports_df

df = create_data()
df['z_duration'] = normalize(df['duration'])
print(df)
z=1

#Add a new column

#Add a column based on others

#Apply a custom spreadsheet function
a=1





