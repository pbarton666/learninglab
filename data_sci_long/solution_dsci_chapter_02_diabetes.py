#solution_dsci_chapter_02_diabetes.py

"""Data from scikit-learn's traing data, and are based on 
   clinical data available here:   
   http://www4.stat.ncsu.edu/~boos/var.select/diabetes.html
   Documentation for this
   and lots of other machine learning sets can be found here:
   http://scikit-learn.org/stable/datasets/index.html
"""   

import sklearn.datasets as ds
import pandas as pd
#everything=ds.load_diabetes()
everything=ds.load_linnerud()

#build DataFrame objects with contents of the data set
eser=pd.DataFrame(everything['data'], columns=everything['feature_names'])
pser=pd.DataFrame(everything['target'], columns=everything['target_names'])
               
#combine the two series a column at a time             
for c in pser.columns:
	eser.assign(c=pser[c], inplace=True)   #alternative:  eser[c]=pser[c]
	x=1

#create an "exercise index"
eser.assign(eindex=eser['Chins'] * 3 + 
                   eser["Situps"] * 2 + 
                   eser["Jumps"])

#convert the Weight to kilos (2.2 lb = 1 kg)
eser['Weight']=eser['Weight']/2.2

#convert Waist to centimeters (1 in = 2.54 cm)
eser['Waist']=eser['Waist']*2.54
x=1