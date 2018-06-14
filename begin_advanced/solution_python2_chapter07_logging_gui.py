#solution_python2_chapter07_logging_gui.py

"""Simple GUI to display database queries.
   An improvement to consider ... wouldn't it
   be nice to have a drop-down list of all the
   valid counties, and have the user be able to
   choose?
"""

from tkinter import *
import logging
from solution_python2_chapter07_logging import \
     get_ale_houses

#grabs the logger
logger=logging.getLogger()

#placeholder database and table values
DB='beer'
TABLE='brewpub'

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        main_frame = Frame(self)
        Label(main_frame, text="Please input a county").pack()
        self.text_in = Entry(main_frame)
        self.text_in.insert("end", "Kent")
        self.text_in.pack()
        self.btn_go=Button(main_frame, text="GO!", command=self.handler)
        self.btn_go.pack()
        self.text_display=Text(main_frame, height= 50, width=50)
        self.text_display.pack()
        main_frame.pack()
        
    def handler(self):
        """Runs a db query and populates the text box"""
        #empty existing content
        self.text_display.delete(0.0, END)
        #get results from the database
        text = self.text_in.get()
        if text:
            results=get_ale_houses(db=DB, table=TABLE, 
                                  is_ale=1, county=text) 
        else:
            results=get_ale_houses(db=DB, table=TABLE, is_ale=1) 
            
        for result in results:
            name, _, county = result 
            self.text_display.insert(END, "{:<25} {:<25}\n"\
                 .format(name, county))
        a=1
root = Tk()
app = Application(master=root)
app.mainloop()
