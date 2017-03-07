#!/usr/bin/env python3
#py_gui_4.py
from tkinter import *

#!/usr/bin/env python3
from tkinter import *

#root container object
root = Tk()
root.geometry("400x300")
root.title("Play with frames")

#a frame as 'child object' to root
f1 = Frame(root, bg="grey")
Label(f1, text="frame 1", bg="grey").pack(side=LEFT)
f1.pack(expand = True, fill=BOTH)

f2 = Frame(root, bg="yellow")
Label(f2, text="frame 2", bg="yellow").pack(side=BOTTOM)
f2.pack(expand=True, fill=BOTH)

f3 = Frame(root, bg="#00ffff")   #alternative specification
Label(f3, text="frame 3", bg="#00ffff").pack(side=RIGHT)
f3.pack(expand=True, fill=BOTH)

f3a = Frame(f3, bg="white")   #alternative specification
Label(f3a, text="subframe 3a", bg="white").pack(side=RIGHT)
f3a.pack(expand=True, fill=BOTH)

root.mainloop()


    

    

	
