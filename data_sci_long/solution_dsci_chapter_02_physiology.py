#solution_dsci_chapter_02_physiology.py

"""Data from scikit-learn's traing data.  There are lots of other machine
   learning data sets here:
   http://scikit-learn.org/stable/datasets/index.html
"""   

import sklearn.datasets as ds
import pandas as pd

everything=ds.load_linnerud()

#build DataFrame objects with contents of the data set
eser=pd.DataFrame(everything['data'], columns=everything['feature_names'])
pser=pd.DataFrame(everything['target'], columns=everything['target_names'])
               
#combine the two series a column at a time  
eser['Weight']  = pser['Weight']
eser['Waist']   = pser['Waist']
eser['Pulse']  = pser['Pulse']

#create an "exercise index"
eser.assign(eindex=eser['Chins'] * 3 + 
                   eser["Situps"] * 2 + 
                   eser["Jumps"])

#convert the Weight to kilos (2.2 lb = 1 kg)
eser['Weight']=eser['Weight']/2.2

#convert Waist to centimeters (1 in = 2.54 cm)
eser['Waist']=eser['Waist']*2.54
