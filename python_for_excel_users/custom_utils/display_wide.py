"""display_wide.py

Routines to support alternative display of pandas objects and images - mostly to
do horizontal display of multiple, related objects for presentations.

"""
from random import random
import matplotlib as mpl
import pandas as pd
import sys
import os

from IPython.core.display import HTML

def display_wide(table_list, titles=None, spacing=0):
    ''' Acceps a list of objects to display horiaontally.  As they are passed from a Jupyter Notebook, the 
        table_list elements are IpyTable objects.  Returns a formatted table with either a title, an image
        or an IpyTable in a cell.
    
        Formats pandas.DataFrame objects directly.  pandas.Series and individual values are first converted
        to pandas.DataFrame objects.  Strings that seem to be image file names (.jpg, etc.) capture images and
        include them in the returned HTML.  File names are assumed to be in the form of /path-to-file/filename 
        relative to the web root of the Jupyter app.
        
        There's little in the way of error checking. Failure to convert to DataFrame is silently
        caught.   Titles, if provided have to be the list-like with the same number of items as the table_list.
        The spacing kwarg represents the number of '&nbsp's inserted between objects rendered.
        
        Objects are displayed horizontally.
    '''
    
    #Build the table incrementally, adding each element of the titles or table_list
    html = '<table>'
    
    #If there are titles, add them as a table
    if titles:
        html +='<tr style="background-color:white;">'
        for t in titles:
            html += '<u><th style="text-align:center;text-decoration:underline;\
                      font-weight: normal;padding:0px;">{}</th></u>'.format(t)
            for _ in range(spacing):
                html += '<td> &nbsp </td>'            
        html += '</tr>'
    
    #Process each element of the table_list according to object type        
    html +='<tr style="background-color:white;">'
    for i in table_list:
        #If it's a DataFrame go ahead and display as html
        if isinstance(i, pd.DataFrame):
            html += '<td >  {} </td>'.format( i._repr_html_())
            
        #If it's a string that smells like an image file name, insert an <img> tag
        elif isinstance(i, str) and \
             os.path.splitext(i)[1].lower() in ('.pdf', '.jpg', '.png', '.bmp'):
            #Adding the random() bit to the URL prevents cached version from loading
            html += '<td>' + '<img src="{}?{}"> </td>'.format(i, str(random()))
        
        #If it's a Series, make a dataframe out of it
        elif isinstance(i, pd.Series):
            html += '<td >  {} </td>'.format( i.to_frame()._repr_html_())
            
        #If it's none of the above, try to make a single-element dataframe.  If that
        #  works, find.  If not, give up.  Row index value is 'value', col index is blank.
        else:
            try:
                i = pd.DataFrame([i], ['value'], columns=[''])
                html += '<td >  {} </td>'.format( i._repr_html_())
            except:
                pass
        #Add spacing between each element 
        for _ in range(spacing):
            html += '<td> &nbsp </td>'

    #Finish off the HTML and return it.
    html +=  '</tr></table>'
    return HTML(html) 
    
def plot_image_save(to_plot, path, height_in=4, width_in=4)    :
    """Trick Jupyter Notebook into creating an image to plot without showing it
         interactively.  The idea is to pass in a pandas object and use its plot()
         method to make a default plot then save it.   The Notebook can then load
         the file using an <img> tag.
         
         This allows behind-the-scenes image rendering to support displaying images
         along with DataFrames in-line, horizontally.
         
         The crux more is toggling the matplotlib backend to "Agg" to shut down rendering
         while the ploto object is created then back to the original value when done.  That
         preserves the Notebook's ability to react to plot() interactively when in 'normal'
         use.
         """
    #Remember original back end the switch to "Agg" to shut down rendering
    backend_ =  mpl.get_backend() 
    mpl.use("Agg")  
    
    #If we already have an object, get rid of it.  This helps to force the browser to refresh
    #  the image interactively.
    
    if os.path.exists(path):
        os.remove(path)
      
    fig = to_plot.plot().figure
    fig.set_size_inches(( width_in, height_in))
    fig.savefig(path)
    
    #Resets the back end to the original.
    mpl.use(backend_) 

    return path

def rescue_stranded_notebook(fn = 'fn', ipynb_version = 4):
    """Problem:  A Jupyter JSON file is saved, but it's not really a notebook.  This
         can happen accidently if you force a browser refresh.  So you're left with
         an unusable pile of code.
         
       Solution: rebuild the notebook from the JSON.
       Not robust.
       """
    import nbformat
    
    raw = nbformat.read(open(fn, 'r'), ipynb_version)
    convert.write(raw, open('recovered.ipynb', 'w'), 'ipynb')
    
    
if __name__=='__main__'    :
    pass
