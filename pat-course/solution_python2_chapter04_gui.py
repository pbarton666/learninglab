from tkinter import *
class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.text_in = Entry(top_frame)
        self.label = Label(top_frame, text="Output label")
        self.text_in.pack()
        self.label.pack()
        self.r = IntVar()
        Radiobutton(top_frame, text="Upper case", variable=self.r, value=1).pack(side=LEFT)
        Radiobutton(top_frame, text="Lower case", variable=self.r, value=2).pack(side=LEFT)
        Radiobutton(top_frame, text="Title case", variable=self.r, value=3).pack(side=LEFT)
        top_frame.pack(side=TOP)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Convert", command=self.handle)
        self.handleb.pack(side=LEFT)
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        text = self.text_in.get()
        operation = self.r.get()
        if operation == 1:
            output = text.upper()
        elif operation == 2:
            output = text.lower()
        elif operation == 3:
            output = text.title()
        else:
            output = "*******"
        self.label.config(text=output)
root = Tk()
app = Application(master=root)
app.mainloop()
