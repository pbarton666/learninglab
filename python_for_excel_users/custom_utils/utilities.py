#utilities.py
"""Contains various utility functions.  Feel free to borrow as desired.
"""
import pandas as pd
from string import ascii_lowercase

class display_w():
    """Display objects in "wide" format (side-by-side) in same output cell.  Note that
         this needs to evaluate objects in the current namespace so needs to be here.
         
       This routine works, but only when embedded in the notebook from which it's called."""

    #This formats the div for each element; can be more fancy if desired.
    html = \
        """<div style="float: left; padding: 30px;"> <p {0} </p>{1}  </div>"""
    
    def __init__(self, *args, **kwargs):
        self.args = args
        print(args)
        
    #Called to display as output in iPython.
    def _repr_html_(self):
        return '\n'.join(self.html.format(a, \
                                          eval(a)._repr_html_())for a in self.args)
    
    #Called when object is asked to represent itself as text in Python.
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))for a in self.args) 
    
def fix_and_display_w(*args):
    """This is designed to accept objects as args, add them to the global namespace, with
        made-up names, then call display_w with the made-up names.   The idea is that 
        display_w() can be relegated to utilitites.
        
        This works - sort of - in that the objects are converted and renedred, but only as text.
        In other words, the objects in play are Python (as opposed to iPython) objects and are not
        appropriately passed through to the HTML rendering machinery.
        
        Not a priority to work out presently, however."""
    obj_names = []
    for ix, obj in enumerate(args):
        if not type(obj) == pd.DataFrame:
            obj = pd.DataFrame(obj)
        global this_name
        this_name = "display_{}".format(ascii_lowercase[ix])
        this_name=obj
        #globals()[this_name]=obj
        obj_names.append(this_name)
    display_w(*obj_names)


def create_sports_data():
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

