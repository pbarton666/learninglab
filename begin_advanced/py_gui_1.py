#py_gui_1.py

from tkinter import *
class Application(Frame):
	def say_hi(self):
		print("Hi there, everyone!")
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		self.QUIT.pack({"side": "left"})
		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello",
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack({"side": "left"})
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
	



