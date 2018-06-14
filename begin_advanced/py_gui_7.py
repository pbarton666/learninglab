#py_gui_7.py
from tkinter import *
from tkinter.messagebox import *

def double_check_vanilla():
    print("You want vanilla and I trust you.")
def double_check_chocloate():
    if askyesno('Check chocolate', 'Sure you want chocolate'):
        print("OK.  Chocolate it is.")
    else:
        print("I didn't think so.")
root = Tk()
root.geometry("200x50")
b1 = Button(root, text="Chocloate", command=double_check_chocloate)
b1.pack(side=TOP)
b2 = Button(root, text="Vanilla", command=double_check_vanilla)
b2.pack(side=TOP)
root.mainloop()

