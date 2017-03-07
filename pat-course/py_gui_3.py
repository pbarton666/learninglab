#!/usr/bin/env python3
#py_gui_3.py
from tkinter import *
    
def report():
    print(txt[status1.get()])
    
master = Tk()
status1 = IntVar()
Label(master, text="What's your favorite team?").pack()
b1 = Button(master, text="Display", command=report)
b1.pack(side=TOP)
txt = ["Cubs", "Cards", "Mets"]
radios = [Radiobutton(master, value=1),
          Radiobutton(master, value=2),
          Radiobutton(master, value=3)]
for radio, s in zip(radios, txt):
    radio["text"] = s
    radio["variable"] = status1
    radio.pack(side=LEFT)
master.mainloop()

	
