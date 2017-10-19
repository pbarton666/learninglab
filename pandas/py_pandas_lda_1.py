#pandas_lda_1
"""Linear Discriminant Analysis with pandas"""

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import scipy
import matplotlib.pyplot as plt #data visualization
import seaborn as sns
import matplotlib.dates as dates #date munging
import csv
import datetime
import math
from py_utils import printme 	#home-made formatting utilities

live=True  #set True to show plots; False to supress

"""
This module focuses on linear discriminant analysis (LDA).  Use LDA when the 
dependent is categorical and independents are continuous.  Use
ANOVA when the situation is reversed.  It requires that the IVs are normally
distributed (not the case for logistical regression and probit.
   
The LDA is a form of Bayesian classification.  It models the membership in 
each class:

   P(X|y=k)
   
 ...as a multivariate Gaussian distribution.  X is the IV vector, y is the DV,
    k is the class.  Using Bayes' transformation, we can use priors:
    
    [ P(X|y=k) * P(y=k) ] / [ SUM_over_i { P(X|y=i) * P(y=i)  } ]
 
 Full description here: http://scikit-learn.org/stable/modules/lda_qda.html
"""

file_name='iris.data.csv'  #Fisher's classic

"""Data characterizes length and width of sepals and petals of Iris types.
   First couple of lines are:
      slength, swidth, plength, pwidth, iclass
	  5.1,3.5,1.4,0.2,Iris-setosa
"""
#create a DataFrame object
df=pd.read_csv(file_name)
iv_names=['slength', 'swidth', 'plength', 'pwidth']
dv_name='iclass'

#the describe() method produces a new DataFrame
printme( df.describe())               #basic descriptives, all cols
printme( df.describe()['pwidth'])     #select only petal width

#We can create categorical descriptions easily:
auto_cats=pd.Categorical.from_array(df['iclass'])
print(auto_cats.describe())

#This adds a new DataFrame column w/ category designations
df['iclass_ix']=auto_cats.codes
printme(df.head(2))
printme(df.tail(2))

#Let's visualize the data so we can get our arms around it
#  a bit better.

#have a look at sepal / petal length scatter using pandas plot.scater() 
ax=df[df.iclass=='Iris-versicolor'].\
    plot.scatter(x='slength', y='swidth', 
                 color='yellow', label='versicolor') 

df[df.iclass=='Iris-setosa'].\
    plot.scatter(x='slength', y='swidth', 
                 color='red', label='setosa',
                 ax=ax)   #use same axes object!

df[df.iclass=='Iris-virginica'].\
    plot.scatter(x='slength', y='swidth', 
                 color='blue', label='virginica', 
                 ax=ax)    #here, too.

ax.set_title("scatter") 

if live: 
    ax.figure.show()

#You can also "throw the spaghetti against the wall" and look
#  at all the scatters and some summary data:
if live:
    pd.tools.plotting.scatter_matrix(df)
    plt.show()

#... and make it even prettier using seaborn (an alternative plotting
#    library).
if live:
    sns.set()
    sns.pairplot(df[['slength', 'swidth', 'plength', 'pwidth', 'iclass']],
                 hue="iclass", 
                 diag_kind="kde")
    sns.plt.show()

#####################

#Linear discriminant analyis assumes that the IVs are normally.
#   distributed technically, multivariate normal.
#   Here's how to do both univariate normalicy tests

#identify a threshhold p-value (small value -> reject H0)
p_target=.05

#  This uses D'Agostino's K-squared:
#     skew_test_z-score ^2 + kurtosis_test_z-score ^2
#  
#  Test loooks for chi^2 distro w/ 2 df - asks 'is shape about right?'
#     H0: distribution is normal  (this is the "null hypothesis")

print("D'Agostino's K-squared test ")
print(" ... fails if p < {}".format(p_target))

#So, are the IVs ("features") individually normal?  Here's the analytical take:
for iv in iv_names:
    data=df[iv]	
    statistic, p =scipy.stats.normaltest(data)
    if p<p_target:
        result='FAILED. SAD!'
    else: result='passed'
    print("\tfeature: {:<10} {:<20} p={:<10}".\
          format(iv, result, round(p,2)))
print()	

#Let's "eyeball" normalicy asssumptions using a grid of plots

#set up the rows/columns for our plot object
cols=3
rows=math.ceil(len(iv_names)/cols) 

#create a plot object
plt.figure()

#loop over our data vectors and create Q-Q charts for each
row=1; col=1; subplot=1
for iv in iv_names:    
    data=df[iv]	                           #grab the data
    plt.subplot(rows, cols, subplot)       #create the subplot object
    scipy.stats.probplot(data, plot=plt)   #stuff it w/ data
    plt.title(iv)                          #give it a nice title
    #reset indices 
    col+=1
    if col>cols: 
        col=1
        row+=1
    subplot+=1

#spruce it up aesthetically 
fig=plt.gcf()   #get current figure - figure object is main container
fig.canvas.set_window_title("Q-Q Charts")
plt.tight_layout() #alternative:  plt.subplots_adjust()  
#live=True
if live: plt.show()

#Let's say that the IVs are reasonably normal - after all, 
#  our data set is pretty large (n=150) so we've got a bit
#  of slack due to the central limit theorum (lots of data ->
#  mean close to population mean)

#apply discrimint analysis to tease out contributions
#    NB this import would typically go at the top of the module
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#convert categorical iclass values to numeric type
iclass_ix=pd.Categorical.from_array(df[dv_name]).codes
# ... and add them as a new DataFrame column
df['iclass_ix']=iclass_ix

#grab the descriptive data
raw_data = df[iv_names].values

#create an instance of LDA.  We'll use this object to run
#  analysis, test results, store the solved model.
lda = LDA(n_components=2)

#use fit() to produce component vectors and transform() to project
lda_result=lda.fit(raw_data, iclass_ix)
lda_result=lda_result.transform(raw_data)

#so, how did we do?  
mean_success_rate=lda.score(raw_data, iclass_ix)
printme("Success rate:", round(mean_success_rate, 2))

#let's have a look:

#these are projections to what we can call "x, y"
df['dim1'] = lda_result[:, 0]
df['dim2'] = lda_result[:, 1]

#query for the separate iris classes
setosa = df.query("iclass=='Iris-setosa'")
versicolor = df.query("iclass=='Iris-versicolor'")
virginica = df.query("iclass=='Iris-virginica'")

#create a new plotting object and load it with KDE (kernel 
#   density estimate) plots
plt.figure()

#these are color pallattes known to seaborn (lots of other options)
color1="Greens"; color2="Purples"; color3="Blues"

ax = sns.kdeplot(setosa.dim1, setosa.dim1, cmap=color1,
                 shade=True, shade_lowest=False)
ax = sns.kdeplot(versicolor.dim1, versicolor.dim2, cmap=color2,
                 shade=True, shade_lowest=False)
ax = sns.kdeplot(virginica.dim1, virginica.dim2, cmap=color3,
                 shade=True, shade_lowest=False)

#create some labels; this picks off the darkest color of each palatte
color1 = sns.color_palette(color1)[-1]
color2 = sns.color_palette(color2)[-1]
color3 = sns.color_palette(color3)[-1]

#this places text (x, y, text, color, font size)
ax.text(5, 4, "Iris setosa", color=color1, size=20)
ax.text(0, 0, "Iris versicolor", color=color2, size=20)
ax.text(-10, 4, "Iris virginica", color=color3, size=20)

#second arg is a dict that can contain lots of font specs
ax.set_title('Linear Discriminant Analysis', {'fontsize':20})
live=True
if live: sns.plt.show()

#But, really, we're cheating.   We've created an "accurate"
#   model, but have no expectation it will work on any other
#   iris data set.  Our model is "overtrained" and brittle.

#moved to sklearn.model_selection in v. 0.18
from sklearn.cross_validation import train_test_split

#could do this manually, but it's built-in.  ".5" makes a 50/50 split
train, test=train_test_split(df, test_size=.5)
lda = LDA(n_components=2)

train_data = train[['slength', 'swidth', 'plength', 'pwidth']].values
train_class_ix=train['iclass_ix']

test_data = test[['slength', 'swidth', 'plength', 'pwidth']].values
test_class_ix=test['iclass_ix']

#use fit() to produce component vectors
train_result=lda.fit(train_data, train_class_ix)
tlda_result=train_result.transform(train_data)

#so, how did we do?  
train_success_rate=train_result.score(train_data, train_class_ix)
printme("Training success rate:", round(train_success_rate, 2))

#This time using test data against trained model
test_success_rate=train_result.score(test_data, test_class_ix)
printme("Test success rate ('naive' data):", round(test_success_rate, 2))


#Not bad.  What impact did the size of the training set have?
results=[]
for training_frac in [.10,.20,.30,.40,.50]:
    train, test=train_test_split(df, test_size=training_frac)
    lda = LDA(n_components=2)
    
    train_data = train[['slength', 'swidth', 'plength', 'pwidth']].values
    train_class_ix=train['iclass_ix']
    
    test_data = test[['slength', 'swidth', 'plength', 'pwidth']].values
    test_class_ix=test['iclass_ix']
    
    #use fit() to produce component vectors
    train_result=lda.fit(train_data, train_class_ix)
    tlda_result=train_result.transform(train_data)
    
    #so, how did we do?  This time using test data against trained model
    test_success_rate=train_result.score(test_data, test_class_ix)
    results.append((training_frac, test_success_rate))

print("results from changing training fraction")
printme("YMMV as the training set is randomly drawn")
fmt="{:<10} {:<10}"
print(fmt.format("fraction", "score"))
print(fmt.format("_"*10, "_"*10))
print()

for frac, result in results:
    print(fmt.format(frac, round(result,2)))


#if you like your model, you can "save it for breakfast"
import pickle

fn='my_lda_model.pkl'
model=train_result

#serialize and store
with open(fn, 'wb') as f:
    pickle.dump(model,f)

#kill the original     
model=None

#reconstitute the Python object
with open(fn, 'rb') as f:
    model=pickle.load(f)
    
printme("recovered model", repr(model))

printme("Same score?")
reconstituted = model.score(test_data, test_class_ix)
original = train_result.score(test_data, test_class_ix)
printme("original: {}   reconstituted: {}".\
        format(original, reconstituted))
   
a=1