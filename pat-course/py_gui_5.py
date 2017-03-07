#py_gui_5.py
from tkinter import *

def placeholder(): print("placeholder event")
file_new=file_close=file_close_all=refactor_rename=\
    refactor_move=placeholder

root = Tk()
menubar = Menu(root)      
root.config(menu=menubar) 

filemenu = Menu(menubar)
filemenu.add_command(label="New", command=file_new)
filemenu.add_separator()
filemenu.add_command(label="Close", command=file_close)
filemenu.add_command(label="Close All",command=file_close_all)

menubar.add_cascade(label="File",menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="Rename Symbol", command=refactor_rename)
editmenu.add_command(label="Move Symbol", command=refactor_move)

menubar.add_cascade(label="Refactor",menu=editmenu)

root.mainloop()
