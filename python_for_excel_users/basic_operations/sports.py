import pandas as pd
import os, sys

outfn_base = 'sports'
excel_ext = '.xlsx'
csv_ext = '.csv'

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

#Save as an Excel workbook and equvalent CSV file
df.to_excel(outfn_base + excel_ext)
df.to_csv(outfn_base + csv_ext)

