#py_gui_8.py

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename

def set_color():
        (rgb_color,hex_color) = askcolor()
        if ( hex_color ):
                print(hex_color, rgb_color)
                btn_color.config(background=hex_color)
def read_file():
        file_to_open = askopenfilename()
        f = open(file_to_open, "r")
        lines = f.readlines()
        for line in lines: text.insert(END, line)

def delete_text(): text.delete(1.0,END)

root = Tk()
btn_color = Button(root, text="Choose a Color",
              command = set_color)
btn_color.config(height=1, font=("Cambria", 10, 'italic'))
btn_color.pack(expand=YES, fill=BOTH)
Button(text="Open File", command=read_file).pack()
Button(text="Clear", command=delete_text).pack()
text = Text(height=10, width=70)
text.pack()
root.mainloop()

