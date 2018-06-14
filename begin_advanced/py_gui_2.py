#!/usr/bin/env python3
#py_gui_2.py
from tkinter import *
class Application(Frame):
	

	def report(self):
		status = [self.status1.get(), self.status2.get(), self.status3.get()]
		print("Checkbox states:", status)
		if not sum(status):
			print("Please select a team.")
			return
		if status[0]:
			print(self.ck1["text"], "GO CUBS!")
			self.ck1.deselect()
		if status[1]:
			print(self.ck2["text"])
			self.ck2.deselect()
		if status[2]:
			print(self.ck3["text"])
			self.ck3.deselect()
		
	def createWidgets(self):
		"populate master frame"
		
		Label(text="Select Favorite Team").pack()   #returns None
		self.b1 = Button(text="List Teams", command=self.report)
		self.b1.pack(side=TOP)
		
		#tkinter IntVar objects are integer-like objects
		self.status1, self.status2, self.status3 = IntVar(), IntVar(), IntVar()
		self.ck1 = Checkbutton(text="Cubs", variable=self.status1)
		self.ck2 = Checkbutton(text="Cards", variable=self.status2)
		self.ck3 = Checkbutton(text="Mets", variable=self.status3)

		self.ck1.pack(side=LEFT)
		self.ck2.pack(side=LEFT)
		self.ck3.pack(side=LEFT)
		
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
	
