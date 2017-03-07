#py_gui_6.py
from tkinter import *
def find_text():
    line = entry_line.get()
    look_for = entry_find.get()  
    data = text.get(line + ".0", END)
    if look_for in data:
        print("Yay, we found {}!".format(look_for))
    else:
        print("Sorry, no {} here.".format(look_for))
def delete_text():
    line = entry_line.get()
    all_text=text.get(line + ".0", END)
    look_for = entry_find.get()
    all_text=all_text.replace(look_for + '\n', '')
    text.delete(line + ".0" , 'end')
    text.insert("end", all_text)

def xgrabtext():
    line = entry_line.get()
    pos = entry_find.get()
    data = text.get(line + "." + pos, END)
    print(data)
def xdeltext():
    text.delete(line + "." + pos, 'end')

root = Tk()
Label(root, text="Starting In This Line:").pack()
entry_line = Entry(root, text='1')
entry_line.pack()
Label(root, text="Find this text").pack()
entry_find = Entry(root, text="Cubs")
entry_find.pack()
b1 = Button(root, text="Find", command=find_text)
b1.pack()
b2 = Button(root, text="Delete", command=delete_text)
b2.pack()
b3 = Button(root, text="Quit", command=root.destroy)
b3.pack()
text = Text(root, height=6, width=50)
text.insert("end", "Cubs\nCards\nMets")
text.pack()

root.mainloop()
